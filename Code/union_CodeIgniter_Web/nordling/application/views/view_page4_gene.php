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

<table style='font-size: 25px;'>
       <tr>
           <th colspan ='4'>使用資料庫</th>
       </tr>

       <tr align='center'>
           <td>Ribo_H_Rep1</td>
           <td>Ribo_H_Rep2</td>
           <td>Ribo_N_Rep1</td>
           <td>Ribo_N_Rep2</td>
       </tr>
</table>
<br><br>
<table style='font-size: 25px;'>
       <tr align='center'>
           <th>Gene</th>
           <th>ID</th>
           <th>Ribo_H_Rep1</th>
           <th>Ribo_H_Rep2</th>
           <th>Ribo_N_Rep1</th>
           <th>Ribo_N_Rep2</th>
           <th>logFC</th>
           <th>P_value</th>
       </tr>
<?php

      for($i=0;$i<count($express);$i++){

        echo "<tr><td>".$express[$i]['COL1']."</td>";
        echo "<td>".$express[$i]['COL2']."</td>";
        echo "<td>".$this->science->change($express[$i]['COL3'])."</td>";
        echo "<td>".$this->science->change($express[$i]['COL4'])."</td>";
        echo "<td>".$this->science->change($express[$i]['COL5'])."</td>";
        echo "<td>".$this->science->change($express[$i]['COL6'])."</td>";
        echo "<td>".$this->science->change($express[$i]['COL7'])."</td>";
        echo "<td>".$this->science->change($express[$i]['COL9'])."</td></tr>";
      }
      echo "</table><br><br>";
?>
  <table style="font-size: 25px;">

              <tr>
                 <th>5'UTR</th>
                 <th>CDS</th>
                 <th>3'UTR</th>
              </tr>

              <tr align="center">
                  <td><img src='http://140.116.215.238/~z7724581/GD1/img/red.jpg' height = "20px"width      = '200px'></td>

                  <td><img src='http://140.116.215.238/~z7724581/GD1/img/blue.jpg' height = "20px"width      = '200px'></td>

                  <td><img src='http://140.116.215.238/~z7724581/GD1/img/yellow.jpg' height = "20px"width      = '200px'></td>
                            
              </tr>
  </table><br><br>

<?php  
  $count = count($data);

  for($i=0;$i<count($data)-4;$i++){
    echo "<table style='font-size: 20px;'>";
    
    
    echo "<tr><th colspan='2' style='background:#94F78F'>".$data[$i]['Isoform']."</th></tr>";

    echo "<tr><th style='background:#94F78F'>SQL</th><th style='background:#94F78F'>IMG</th></tr>";

    echo "<tr><th style='background:#94F78F'>ribo_h1</th>";
    echo "<td><a><img src=".base_url('gd_img')."/gene_level2_ribo_h1_".$data[$i]['Isoform']."_".$data[$i]['Gene']."_".$rand.".jpg"."></a></td></tr>";

    echo "<tr><th style='background:#94F78F'>ribo_h2</th>";
    echo "<td><a><img src=".base_url('gd_img')."/gene_level2_ribo_h2_".$data[$i]['Isoform']."_".$data[$i]['Gene']."_".$rand.".jpg"."></a></td></tr>";

    echo "<tr><th style='background:#94F78F'>ribo_n1</th>";
    echo "<td><a><img src=".base_url('gd_img')."/gene_level2_ribo_n1_".$data[$i]['Isoform']."_".$data[$i]['Gene']."_".$rand.".jpg"."></a></td></tr>";

    echo "<tr><th style='background:#94F78F'>ribo_n2</th>";
    echo "<td><a><img src=".base_url('gd_img')."/gene_level2_ribo_n2_".$data[$i]['Isoform']."_".$data[$i]['Gene']."_".$rand.".jpg"."></a></td></tr>";
   
   

    echo "</table><br><br>";
    }
    

   ?>

  </body>
</html>