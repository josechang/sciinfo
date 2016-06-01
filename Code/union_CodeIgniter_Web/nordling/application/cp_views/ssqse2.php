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
      <table style="font-size: 20px;">
          
          <tr>
             <th>Gene</th>
             <th>Isoform</th>
             <th>Ribo_H_Rep1_CPM</th>
             <th>Ribo_H_Rep2_CPM</th>
             <th>Ribo_N_Rep1_CPM</th>
             <th>Ribo_N_Rep2_CPM</th>
             <th>Fold_change</th>
             <th>P_value</th>
          </tr> 


              <?php  
                    if(!empty($data[0])){
                       
                       
                       $arr_c=[];
                       for($i=0;$i<count($data);$i++){
                         if(!empty($data[$i]['COL1'])){
                            $a1=$data[$i]['COL1'];
                            array_push($arr_c, $a1);
                         }
                       }

                       $answer = array_count_values($arr_c);

                       // echo "<pre>";
                       // print_r($answer);

                       $f1=0;
                       $f2=0;
                       for($i=0;$i<count($data);$i++){
                         if(!empty($data[$i]['COL1'])){

                          $a1=$data[$i]['COL1'];

                          $time=$answer[$a1] ;
                          // echo "~~~~~".$time."~~".$a1;
                          // if($time !=1){
                          //    $f +=1;
                          //  }else{
                          //    $f =0;
                          //  }
                           

                          // echo $time ."--".$f1."<br>";
                          if($f1==0){
                           echo "<tr><td rowspan=".$time."><a href='/~z7724581/GD1/index.php/user/ch_gene1/".$a1."/Ribo_N_vs_H'.' target='_blank'>".$data[$i]['COL1']."</a></td>
                                ";
                          }
                          $f1 +=1;
                          if($time == $f1){
                             $f1 =0 ;
                           }

                           $a2=$data[$i]['COL2'];
                          echo "<td><a href='/~z7724581/GD1/index.php/user/ch_id1/".$a1."/".$a2."/Ribo_N_vs_H'.' target='_blank'>".$data[$i]['COL2']."</a></td>"; 


                           










                          // echo "<tr><td><a href='/~z7724581/GD1/index.php/user/ch_gene1/".$a1."/Ribo_N_vs_H'.' target='_blank'>".$data[$i]['COL1']."</a></td>";
                         
                          echo "<td>".round($data[$i]['COL3'],3)."</td>"; 
                          echo "<td>".round($data[$i]['COL4'],3)."</td>"; 
                          echo "<td>".round($data[$i]['COL5'],3)."</td>"; 
                          echo "<td>".round($data[$i]['COL6'],3)."</td>"; 
                          echo "<td>".round($data[$i]['COL7'],3)."</td>"; 
                          echo "<td>".round($data[$i]['COL9'],3)."</td></tr>"; 
                          
                         }
                       }                 
                    }           
              ?>
        </table>
 

   <div id="msg2" style="display: none"></div>


</body>
</html>