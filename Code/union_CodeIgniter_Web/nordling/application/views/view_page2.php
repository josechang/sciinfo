<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<link rel="stylesheet" href="http://140.116.215.238/~z7724581/GD/css/z1.css" />  

<style type="text/css">
        
        table {
              margin: 0 auto;
              width:  1520px;

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
     $name=str_replace("[", "", $name);
     $name=str_replace("'", "", $name);
     $name=str_replace("]", "", $name);
     $ex_name=explode(",", $name);
     
     $check1=$check;
     unset($check1['search']);
     $key= array_keys($check1);
     for($j=0;$j<count($key);$j++){
          
      for($i=0;$i<count($ex_name);$i++){
         
         $file   ="/home/z7724581/public_html/nordling/python/TXT/".ltrim(rtrim($ex_name[$i]))."_".$key[$j].".txt";
         $myfile = fopen($file, "r") or die("Unable to open file!");

         while(!feof($myfile)) {
                echo fgets($myfile) . "<br>";
         }
         fclose($myfile);
         
         echo "------------------------------------------";
         echo "<br>" ."<br>" ."<br>";

      }
     }
?>

  </body>
</html>