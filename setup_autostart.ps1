# PowerShell script to set up autostart for Filament Manager
# Run this as Administrator

param(
    [string]$Method = "startup"  # Options: "startup", "taskscheduler", "remove"
)

$AppName = "3D Printer Filament Manager"
$AppPath = "C:\Users\james\Workspace\3d_printer_filament_manager"
$BatchFile = "$AppPath\start_filament_manager_silent.bat"
$StartupFolder = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup"

function Add-ToStartupFolder {
    Write-Host "Adding to Windows Startup folder..." -ForegroundColor Green
    
    # Create shortcut to the batch file
    $ShortcutPath = "$StartupFolder\$AppName.lnk"
    $WshShell = New-Object -comObject WScript.Shell
    $Shortcut = $WshShell.CreateShortcut($ShortcutPath)
    $Shortcut.TargetPath = $BatchFile
    $Shortcut.WorkingDirectory = $AppPath
    $Shortcut.Description = "3D Printer Filament Manager - Auto Start"
    $Shortcut.Save()
    
    Write-Host "✓ Added shortcut to startup folder: $ShortcutPath" -ForegroundColor Green
    Write-Host "The Filament Manager will now start automatically when you log in." -ForegroundColor Yellow
}

function Add-ToTaskScheduler {
    Write-Host "Setting up Task Scheduler..." -ForegroundColor Green
    
    # Create a scheduled task
    $Action = New-ScheduledTaskAction -Execute $BatchFile -WorkingDirectory $AppPath
    $Trigger = New-ScheduledTaskTrigger -AtLogon -User $env:USERNAME
    $Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
    $Principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive
    
    $Task = New-ScheduledTask -Action $Action -Trigger $Trigger -Settings $Settings -Principal $Principal -Description "Auto-start 3D Printer Filament Manager"
    
    try {
        Register-ScheduledTask -TaskName $AppName -InputObject $Task -Force
        Write-Host "✓ Created scheduled task: $AppName" -ForegroundColor Green
        Write-Host "The Filament Manager will now start automatically when you log in." -ForegroundColor Yellow
    }
    catch {
        Write-Host "✗ Failed to create scheduled task. You may need to run as Administrator." -ForegroundColor Red
        Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
    }
}

function Remove-AutoStart {
    Write-Host "Removing autostart configurations..." -ForegroundColor Yellow
    
    # Remove from startup folder
    $ShortcutPath = "$StartupFolder\$AppName.lnk"
    if (Test-Path $ShortcutPath) {
        Remove-Item $ShortcutPath -Force
        Write-Host "✓ Removed startup folder shortcut" -ForegroundColor Green
    }
    
    # Remove from task scheduler
    try {
        Unregister-ScheduledTask -TaskName $AppName -Confirm:$false -ErrorAction Stop
        Write-Host "✓ Removed scheduled task" -ForegroundColor Green
    }
    catch {
        Write-Host "ℹ No scheduled task found to remove" -ForegroundColor Gray
    }
    
    Write-Host "Autostart has been disabled." -ForegroundColor Yellow
}

function Show-Status {
    Write-Host "`n=== Autostart Status ===" -ForegroundColor Cyan
    
    # Check startup folder
    $ShortcutPath = "$StartupFolder\$AppName.lnk"
    if (Test-Path $ShortcutPath) {
        Write-Host "✓ Startup folder: ENABLED" -ForegroundColor Green
    } else {
        Write-Host "✗ Startup folder: DISABLED" -ForegroundColor Red
    }
    
    # Check task scheduler
    try {
        $Task = Get-ScheduledTask -TaskName $AppName -ErrorAction Stop
        Write-Host "✓ Task Scheduler: ENABLED" -ForegroundColor Green
    }
    catch {
        Write-Host "✗ Task Scheduler: DISABLED" -ForegroundColor Red
    }
    
    Write-Host "`nFilament Manager URL: http://localhost:8847" -ForegroundColor Cyan
}

# Main logic
switch ($Method.ToLower()) {
    "startup" {
        Write-Host "Setting up autostart using Windows Startup folder..." -ForegroundColor Cyan
        Add-ToStartupFolder
    }
    "taskscheduler" {
        Write-Host "Setting up autostart using Task Scheduler..." -ForegroundColor Cyan
        Add-ToTaskScheduler
    }
    "remove" {
        Remove-AutoStart
    }
    "status" {
        Show-Status
    }
    default {
        Write-Host "Usage: .\setup_autostart.ps1 [startup|taskscheduler|remove|status]" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "Options:" -ForegroundColor Cyan
        Write-Host "  startup       - Add to Windows startup folder (default)" -ForegroundColor White
        Write-Host "  taskscheduler - Use Task Scheduler (more reliable)" -ForegroundColor White  
        Write-Host "  remove        - Remove all autostart configurations" -ForegroundColor White
        Write-Host "  status        - Show current autostart status" -ForegroundColor White
        Write-Host ""
        Write-Host "Examples:" -ForegroundColor Cyan
        Write-Host "  .\setup_autostart.ps1" -ForegroundColor Gray
        Write-Host "  .\setup_autostart.ps1 taskscheduler" -ForegroundColor Gray
        Write-Host "  .\setup_autostart.ps1 remove" -ForegroundColor Gray
    }
}

Show-Status