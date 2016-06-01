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

    echo "<table style='font-size: 20px;'>";
    
    $count = count($isoform_data);
    echo "<tr><th colspan='9'>Ribo_H_vs_N</th></tr>";
  
    echo "<tr><th>Gene</th>";
    echo "<th>Isoform</th>";
    echo "<th>Ribo_H_Rep1</th>";
    echo "<th>Ribo_H_Rep2</th>";
    echo "<th>Ribo_N_Rep1</th>";
    echo "<th>Ribo_N_Rep2</th>";
    echo "<th>Total</th>";
    echo "<th>Fold_change</th>";
    echo "<th>P_Value</th></tr>";

    // echo "<pre>";
    // print_r($isoform_data);
    for($i=0;$i<$count;$i++){
      if($i==0){
        echo "<tr><td rowspan='".$count."''><a href='/~z7724581/GD1/index.php/user/gene_img_ribo/new_ribo_H_vs_N_Gene_Level/new_ribo_H_vs_N_Isoform_Level/".$isoform_data[0]['Gene']."/'.'>".$isoform_data[0]['Gene']."</a>"."</td>";
        
        echo "<td><a href='/~z7724581/GD1/index.php/user/id_img_ribo/new_ribo_H_vs_N_Gene_Level/new_ribo_H_vs_N_Isoform_Level/".$isoform_data[0]['Gene']."~".$isoform_data[0]['Isoform']."/'.'>" .$isoform_data[0]['Isoform']."</a></td>";
      }else{
        echo "<td><a href='/~z7724581/GD1/index.php/user/id_img_ribo/new_ribo_H_vs_N_Gene_Level/new_ribo_H_vs_N_Isoform_Level/".$isoform_data[$i]['Gene']."~".$isoform_data[$i]['Isoform']."/'.'>" .$isoform_data[$i]['Isoform']."</a></td>";
      }    
      
      echo     "<td>".$this->science->change($isoform_data[$i]['Ribo_H1'])."</td>";
      echo     "<td>".$this->science->change($isoform_data[$i]['Ribo_H2'])."</td>";
      echo     "<td>".$this->science->change($isoform_data[$i]['Ribo_N1'])."</td>";
      echo     "<td>".$this->science->change($isoform_data[$i]['Ribo_N2'])."</td>";

      $plus = $this->science->change($isoform_data[$i]['Ribo_H1'])
              +$this->science->change($isoform_data[$i]['Ribo_H2'])
              +$this->science->change($isoform_data[$i]['Ribo_N1'])
              +$this->science->change($isoform_data[$i]['Ribo_N2']);

      echo     "<td>".$plus."</td>";
      echo     "<td>".$this->science->change($isoform_data[$i]['Fold_change'])."</td>";
      echo     "<td>".$this->science->change($isoform_data[$i]['P_Value'])."</td></tr>";
        
    }
    echo "</table>";

   ?>


<!-- <img src="smiley.gif" alt="Smiley face" width="42" height="42"> -->
  </body>
</html>