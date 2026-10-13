# Chuyển tệp kết quả (.docx bằng Word, một trang tính .xlsx bằng Excel) sang PDF để chụp ảnh nối vào cuối video.
# Cách dùng: powershell -File sang_pdf.ps1 <tệp nguồn> <tệp pdf> [tên trang tính]
param([string]$Nguon, [string]$Ra, [string]$Trang = '')
if ($Nguon.ToLower().EndsWith('.docx')) {
    $w = New-Object -ComObject Word.Application; $w.Visible = $false
    $d = $w.Documents.Open($Nguon, $false, $true); $d.ExportAsFixedFormat($Ra, 17); $d.Close($false); $w.Quit()
} else {
    $x = New-Object -ComObject Excel.Application; $x.Visible = $false; $x.DisplayAlerts = $false
    $b = $x.Workbooks.Open($Nguon, 0, $true)
    $s = if ($Trang) { $b.Worksheets.Item($Trang) } else { $b.Worksheets.Item(1) }
    $s.PageSetup.Orientation = 2; $s.PageSetup.Zoom = $false; $s.PageSetup.FitToPagesWide = 1; $s.PageSetup.FitToPagesTall = $false
    $s.ExportAsFixedFormat(0, $Ra); $b.Close($false); $x.Quit()
}
