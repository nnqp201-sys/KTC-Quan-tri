param([string]$ThuMuc)
$x = New-Object -ComObject Excel.Application
$x.Visible = $false; $x.DisplayAlerts = $false
try {
  Get-ChildItem -LiteralPath $ThuMuc -Recurse -Filter *.xlsx | ForEach-Object {
    $w = $x.Workbooks.Open($_.FullName); $x.CalculateFull(); $w.Save(); $w.Close($false)
    Write-Output ("TINH " + $_.Name)
  }
} finally { $x.Quit(); [void][Runtime.InteropServices.Marshal]::ReleaseComObject($x) }
