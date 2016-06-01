<?php 

class sql extends CI_Model{

    public function get($data){  

          $this->load->database();
          
          $sql_name=[];
          $Ribo=['Ribo_H_Rep1','Ribo_H_Rep2','Ribo_N_Rep1','Ribo_N_Rep2'];
          if(in_array('Ribo_N_vs_H',array_keys($data))){
          	 for($i=0;$i<count($Ribo);$i++){
               array_push($sql_name,$Ribo[$i]);
             }

          }      
             


          if($data['radio'] == 'radio1'){
                     if($data['select1'] == 'case1'){
                        $case = "COL7 >= " . $data['text1'];

                      }elseif($data['select1'] == 'case2'){
                         $case = "COL7 <= " . $data['text1'];
                     }
                     
              
               }elseif($data['radio'] == 'radio2'){
             
                   $number = pow(10,$data['text2']);
                        
                   if($data['select2'] == 'case1'){ 

                        $case = "COL9 >= " . $number;
                   }elseif($data['select2'] == 'case2'){ 

                        $case = "COL9 <= " . $number;
                   }
                      
               }
           
           $combine = 'SELECT * FROM '. 'Ribo_N_vs_H '.'WHERE '. $case .' order by COL1';
           $get_id= $this->db->query($combine);
           $get_id_data=$get_id->result_array();
           $get_id_data['sql'] ='Ribo_N_vs_H';
           return($get_id_data);

    }
}
?>