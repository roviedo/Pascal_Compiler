

Procedure BubbleSort(numbers : Array of Integer; size : Integer);
Var i, j, temp :  Integer;


Begin
   For i := size-1 DownTo 1 do
      For j := 2 to i do
	    If (numbers[j-1] > numbers[j]) then
	    Begin
	       temp := numbers[j-1];
	       numbers[j-1] := numbers[j];
	       numbers[j] := temp;
	    End;

End.