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
  // echo "<pre>";
  // print_r($isoform_data);
  $count = count($data);
  // echo $count;
  for($i=0;$i<count($data)-8;$i++){
    echo "<table style='font-size: 20px;'>";
    
    
    echo "<tr><th colspan='2'>".$data[$i]['Isoform']."</th></tr>";

    echo "<tr><th>SQL</th><th>IMG</th></tr>";

    echo "<tr><th>ribo_h1</th>";
    echo "<td><a><img src=".base_url('gd_img')."/gene_level_ribo_h1_".$data[$i]['Isoform']."_".$data[$i]['Gene']."_".$rand.".jpg"."></a></td></tr>";

    echo "<tr><th>ribo_h2</th>";
    echo "<td><a><img src=".base_url('gd_img')."/gene_level_ribo_h2_".$data[$i]['Isoform']."_".$data[$i]['Gene']."_".$rand.".jpg"."></a></td></tr>";

    echo "<tr><th>ribo_n1</th>";
    echo "<td><a><img src=".base_url('gd_img')."/gene_level_ribo_n1_".$data[$i]['Isoform']."_".$data[$i]['Gene']."_".$rand.".jpg"."></a></td></tr>";

    echo "<tr><th>ribo_n2</th>";
    echo "<td><a><img src=".base_url('gd_img')."/gene_level_ribo_n2_".$data[$i]['Isoform']."_".$data[$i]['Gene']."_".$rand.".jpg"."></a></td></tr>";
   
   

    echo "</table><br><br>";
    }
    

   ?>


<!-- <img src="smiley.gif" alt="Smiley face" width="42" height="42"> -->
  </body>
</html>