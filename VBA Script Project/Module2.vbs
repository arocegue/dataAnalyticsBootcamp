Sub moduleTwo():

Dim rowCount As Integer
Dim summaryRow As Integer
Dim annualInitial As Double
Dim totalVolume As LongLong

    For Each ws In Worksheets
        'One iteration
        summaryRow = 2
        'Last Row index
        LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
        'Begin Column Headers
        ws.Cells(1, 9).Value = "Ticker"
        ws.Cells(1, 10).Value = "Yearly Change"
        ws.Cells(1, 11).Value = "Percent Change"
        ws.Cells(1, 12).Value = "Total Stock Volume"



        'Declare open price
        annualInitial = ws.Cells(2, 3).Value
        'Declare volume
        totalVolume = 0
        For x = 2 To LastRow
            totalVolume = totalVolume + ws.Cells(x, 7).Value
            If ws.Cells(x + 1, 1).Value <> ws.Cells(x, 1).Value Then
                ws.Cells(summaryRow, 9).Value = ws.Cells(x, 1).Value
                ws.Cells(summaryRow, 10).Value = ws.Cells(x, 6).Value - annualInitial
                If ws.Cells(summaryRow, 10).Value >= 0 Then
                    ws.Cells(summaryRow, 10).Interior.ColorIndex = 4
                Else
                    ws.Cells(summaryRow, 10).Interior.ColorIndex = 3
                End If
                ws.Cells(summaryRow, 11).Value = (ws.Cells(x, 6).Value - annualInitial) / annualInitial
                ws.Cells(summaryRow, 12).Value = totalVolume
                annualInitial = ws.Cells(x + 1, 3).Value
                summaryRow = summaryRow + 1
                totalVolume = 0
            End If
        Next x


        ws.Range("$K2:K" & (summaryRow - 1)).NumberFormat = "0.00%"
        ws.Range("$L2:L" & (summaryRow - 1)).NumberFormat = "0"
        ws.Range("$J2:J" & (summaryRow - 1)).NumberFormat = "0.00"



        ws.Cells(1, 15).Value = "Ticker"
        ws.Cells(1, 16).Value = "Value"

        ws.Cells(2, 14).Value = "Greatest % Increase"
        ws.Cells(3, 14).Value = "Greatest % Decrease"
        ws.Cells(4, 14).Value = "Greatest Total Volume"
        For y = 2 To summaryRow - 1
            If ws.Cells(y, 11).Value > ws.Cells(2, 16).Value Then
                ws.Cells(2, 16).Value = ws.Cells(y, 11).Value
                ws.Cells(2, 15).Value = ws.Cells(y, 9).Value
            ElseIf ws.Cells(y, 11).Value < ws.Cells(3, 16).Value Then
                ws.Cells(3, 16).Value = ws.Cells(y, 11).Value
                ws.Cells(3, 15).Value = ws.Cells(y, 9).Value
            End If
            If ws.Cells(y, 12).Value > ws.Cells(4, 16).Value Then
                ws.Cells(4, 16).Value = ws.Cells(y, 12).Value
                ws.Cells(4, 15).Value = ws.Cells(y, 9).Value
    
            End If
        Next y
    
        ws.Range("$P2:$P3").NumberFormat = "0.00%"
        ws.Range("$N2:$N4").NumberFormat = "@"
        ws.Range("$P4").NumberFormat = "0"
        ws.Columns("I:P").AutoFit
    Next ws
End Sub

