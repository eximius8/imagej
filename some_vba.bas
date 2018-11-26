Sub Setup_cells()

Dim i, j As Integer

For i = 152 To 401
  For j = 156 To 283
    If Cells(i, 1).Value = Cells(j, 14).Value And Cells(i, 2).Value = Cells(j, 25).Value Then
      Cells(i, 4).Value = Cells(j, 17).Value
      Cells(i, 3).Value = Cells(j, 17).Value * Cells(j, 22).Value * 0.001
    End If
  Next j
Next i
End Sub
