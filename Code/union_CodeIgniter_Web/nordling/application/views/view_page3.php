<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<link rel="stylesheet" href="http://140.116.215.238/~z7724581/GD/css/z1.css" />  

<style type="text/css">
        
        table {
              margin: 0 auto;
              width:  1520px;
              font-size: 25px;

        }
        th {
            background: #E85B5B;
        }
        td{
            background: #F5F5F8;
        }

        #show_sql th{
           background: #989BE6;   

        }
        #show_id th{
           background: #989BE6;      
        }

        #range{
              margin-left: 71%;
        }

        #goToTop {
                            position: fixed;
                            width: 100px;
                            height: 30px;
                            background: #FCEFA1;
                            text-align: none;
                            border: 2px black solid;
                            bottom: 60px;
                            right: 2%;
                         }
        #goback {
                            position: fixed;
                            width: 100px;
                            height: 30px;
                            background: #FCEFA1;
                            text-align: none;
                            border: 2px black solid;
                            bottom: 10px;
                            right: 2%;
                         }




</style>

</head>

<body>

<th colspan="">

  <?php  

      $search=str_replace("__", " ", $search);
      $name=str_replace("__", " ", $name);

     // $name=str_replace("[", "", $name);
     // $name=str_replace("'", "", $name);
     // $name=str_replace("]", "", $name);
     // $ex_name=explode(",", $name);
     
     // $check1=$check;
     // unset($check1['search']);
     // $key= array_keys($check1);
     // for($j=0;$j<count($key);$j++){
          
      for($i=0;$i<count($name);$i++){

              
         $file   ="/home/z7724581/public_html/nordling/python/TXT/".$name[$i]."_result.txt";

         $myfile = fopen($file, "r") or die("Unable to open file!");
         
         $arr ="x".$i;
         $$arr=[];
         while(!feof($myfile)) {
                array_push($$arr,fgets($myfile));
         }
         fclose($myfile);
      }
      // var_dump($x1);
      for($i=0;$i<count($name);$i++){
        echo "<table>";
          echo "<tr>" ;
            echo "<th colspan='2'>" .$name[$i] ."</th>";
          echo "<tr>" ;
            $arr ="x".$i;
            $arr1=$$arr;

            $c1=0;$c2=0;$c3=0;$c4=0;$c5=0;
            $c6=0;$c7=0;$c8=0;$c9=0;
            
            
            
            for($j=0;$j<count($arr1);$j++){
                 
                 // abstract
                 if(ltrim(rtrim($arr1[$j])) == "start_abstract"){
                    $c1=1;
                 }elseif($c1 ==1){

                    echo "<tr><td style='background-color:#A2FB96;text-align:center;'>Abstract line numbers</td><td>".$arr1[$j]."</td></tr>";
                    $c1+=1;
                    echo "<tr><td colspan='2'>" ;

                 }elseif(ltrim(rtrim($arr1[$j])) == "end_abstract"){
                    echo "</td></tr>" ;
                    $c1=0;
                 }elseif($c1 >1){
                    echo $arr1[$j]."<br>";

                 }
                 
                 // introduction
                 if(ltrim(rtrim($arr1[$j])) == "start_introduction"){
                    $c2=1;
                 }elseif($c2 ==1){

                    echo "<tr><td style='background-color:#A2FB96;text-align:center;'>Introduction line numbers</td><td>".$arr1[$j]."</td></tr>";
                    $c2+=1;
                    echo "<tr><td colspan='2'>" ;

                 }elseif(ltrim(rtrim($arr1[$j])) == "end_introduction"){
                    echo "</td></tr>" ;
                    $c2=0;
                 }elseif($c2 >1){
                    echo $arr1[$j]."<br>";

                 }

                 // theoretical
                 if(ltrim(rtrim($arr1[$j])) == "start_theoretical"){
                    $c3=1;
                 }elseif($c3 ==1){

                    echo "<tr><td style='background-color:#A2FB96;text-align:center;'>Theoretical line numbers</td><td>".$arr1[$j]."</td></tr>";
                    $c3+=1;
                    echo "<tr><td colspan='2'>" ;

                 }elseif(ltrim(rtrim($arr1[$j])) == "end_theoretical"){
                    echo "</td></tr>" ;
                    $c3=0;
                 }elseif($c3 >1){
                    echo $arr1[$j]."<br>";

                 }

                 // method
                 if(ltrim(rtrim($arr1[$j])) == "start_method"){
                    $c4=1;
                 }elseif($c4 ==1){

                    echo "<tr><td style='background-color:#A2FB96;text-align:center;'>Method line numbers</td><td>".$arr1[$j]."</td></tr>";
                    $c4+=1;
                    echo "<tr><td colspan='2'>" ;

                 }elseif(ltrim(rtrim($arr1[$j])) == "end_method"){
                    echo "</td></tr>" ;
                    $c4=0;
                 }elseif($c4 >1){
                    echo $arr1[$j]."<br>";

                 }

                 // result
                 if(ltrim(rtrim($arr1[$j])) == "start_result"){
                    $c5=1;
                 }elseif($c5 ==1){

                    echo "<tr><td style='background-color:#A2FB96;text-align:center;'>Result line numbers</td><td>".$arr1[$j]."</td></tr>";
                    $c5+=1;
                    echo "<tr><td colspan='2'>" ;

                 }elseif(ltrim(rtrim($arr1[$j])) == "end_result"){
                    echo "</td></tr>" ;
                    $c5=0;
                 }elseif($c5 >1){
                    echo $arr1[$j]."<br>";

                 }

                 // discussion
                 if(ltrim(rtrim($arr1[$j])) == "start_discussion"){
                    $c6=1;
                 }elseif($c6 ==1){

                    echo "<tr><td style='background-color:#A2FB96;text-align:center;'>Discussion line numbers</td><td>".$arr1[$j]."</td></tr>";
                    $c6+=1;
                    echo "<tr><td colspan='2'>" ;

                 }elseif(ltrim(rtrim($arr1[$j])) == "end_discussion"){
                    echo "</td></tr>" ;
                    $c6=0;
                 }elseif($c6 >1){
                    echo $arr1[$j]."<br>";

                 }

                 // conclusion
                 if(ltrim(rtrim($arr1[$j])) == "start_conclusion"){
                    $c7=1;
                 }elseif($c7 ==1){

                    echo "<tr><td style='background-color:#A2FB96;text-align:center;'>Conclusion line numbers</td><td>".$arr1[$j]."</td></tr>";
                    $c7+=1;
                    echo "<tr><td colspan='2'>" ;

                 }elseif(ltrim(rtrim($arr1[$j])) == "end_conclusion"){
                    echo "</td></tr>" ;
                    $c7=0;
                 }elseif($c7 >1){
                    echo $arr1[$j]."<br>";

                 }
                 
                 // reference
                 if(ltrim(rtrim($arr1[$j])) == "start_reference"){
                    $c8=1;
                 }elseif($c8 ==1){

                    echo "<tr><td style='background-color:#A2FB96;text-align:center;'>Reference line numbers</td><td>".$arr1[$j]."</td></tr>";
                    $c8+=1;
                    echo "<tr><td colspan='2'>" ;

                 }elseif(ltrim(rtrim($arr1[$j])) == "end_reference"){
                    echo "</td></tr>" ;
                    $c8=0;
                 }elseif($c8 >1){
                    echo $arr1[$j]."<br>";

                 }

            }
            echo "</table> <br><br>";



     }
?>

  </body>
</html>