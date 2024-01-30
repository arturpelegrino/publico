Attribute VB_Name = "descobrirPath"
Private Function Local_Workbook_Name(ByRef wb As Workbook) As String

  Dim Ctr As Long
  Dim objShell As Object
  Dim UserProfilePath As String

  'Check if it looks like a OneDrive location
  If InStr(1, wb.FullName, "https://", vbTextCompare) > 0 Then

    'Replace forward slashes with back slashes
    Local_Workbook_Name = Replace(wb.FullName, "/", "\")

    'Get environment path using vbscript
    Set objShell = CreateObject("WScript.Shell")
    UserProfilePath = objShell.ExpandEnvironmentStrings("%UserProfile%")

      'Trim OneDrive designators
    For Ctr = 1 To 4
       Local_Workbook_Name = Mid(Local_Workbook_Name, InStr(Local_Workbook_Name, "\") + 1)
    Next

      'Construct the name
    Local_Workbook_Name = UserProfilePath & "\OneDrive\" & Local_Workbook_Name

  Else

    Local_Workbook_Name = wb.FullName

  End If
  
  Local_Workbook_Name = Local_Workbook_Name

End Function

Private Sub testy()

  Debug.Print Local_Workbook_Name(ActiveWorkbook)

End Sub
