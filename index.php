<form action="#" method="POST">
<input type="text" name="sen">
<input type="submit" value="Predict">
</form>
<br>
<?php

if(isset($_POST['sen']))
{
$sen=$_POST['sen'];
}
if(isset($sen)){
$output = shell_exec('python main1.py '.$sen);
#print(strval($output));
$color="none";
switch(strval($output))
{
		case 0:	
					$emoji="❤️";
					break;
		
		case 1:   $emoji="⚾";
					break;
		
		case 2:   $emoji="😀";
					break;
		
		case 3:	$emoji="😞";
					break;
		
		case 4:   $emoji="🍴";
					break;
		
		case 5:  $emoji="&#128077;&#127995;";
					break;
		default :
					
					$emoji="&#128512;";
}

	$html_em = $sen ." ".$emoji;

print($html_em);
}
?>