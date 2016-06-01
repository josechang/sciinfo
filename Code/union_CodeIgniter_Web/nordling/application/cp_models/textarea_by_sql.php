<?php 

class textarea_by_sql extends CI_Model{

      public function get_data($data){  

          // echo "MODEL-----------------------------------";
          // print_r($data);
          $rand =$data['rand'];
          $this->load->database();
          
          // var_dump($data['mytextarea']);
          $sql_name =$data['sql'][0];         
          if($data['radio'] == 'radio1'){
                     if($data['select1'] == 'case1'){
                         $case = "COL7 > " . $data['text1'];
                     }elseif($data['select1'] == 'case2'){
                        $case = "COL7 < " . $data['text1'];
                      }elseif($data['select1'] == 'case3'){
                        $case = "COL7 >= " . $data['text1'];
                      }elseif($data['select1'] == 'case4'){
                         $case = "COL7 <= " . $data['text1'];
                     }
              
               }elseif($data['radio'] == 'radio2'){
             
                   $number = pow(10,$data['text2']);
                        
                    if($data['select2'] == 'case1'){ 

                        $case = "COL9 > " . $number;
                   }elseif($data['select2'] == 'case2'){ 

                        $case = "COL9 < " . $number;
                   }elseif($data['select2'] == 'case3'){ 

                        $case = "COL9 >= " . $number;
                   }elseif($data['select2'] == 'case4'){ 

                        $case = "COL9 <= " . $number;
                    }      
               }

          if(!empty($data['mytextarea'])){  

               
               $ck = str_replace("\n","' or COL1 = '",$data['mytextarea']);
                   
               $combine = 'SELECT * FROM '. $sql_name .' WHERE '. '(COL1=\''. $ck .'\') and '. $case;
               // echo $combine;
               $get_id= $this->db->query($combine);
               $get_id_data=$get_id->result_array();
              

          }else{
                if(!empty($data['mytext'][0])){
                  
                  $imp1 = implode("' or COL2 = '",$data['1_ck']);
                  $combine1 = 'SELECT * FROM '. $sql_name .' WHERE '. '(COL2=\''. $imp1 .'\') and '. $case;
              
                  $get_id1= $this->db->query($combine1);
                  $get_id1_data=$get_id1->result_array();

                  $get_id_data['id1']=$get_id1_data;
                  // print_r($get_id1_data);
                }
                if(!empty($data['mytext'][1])){

                  $imp2 = implode("' or COL2 = '",$data['2_ck']);
                  $combine2 = 'SELECT * FROM '. $sql_name .' WHERE '. '(COL2=\''. $imp2 .'\') and '. $case;
              
                  $get_id2= $this->db->query($combine2);
                  $get_id2_data=$get_id2->result_array();
                  
                  $get_id_data['id2']=$get_id2_data;
                  // print_r($get_id2_data);
                }
                if(!empty($data['mytext'][2])){
                  $imp3 = implode("' or COL2 = '",$data['3_ck']);
                  $combine3 = 'SELECT * FROM '. $sql_name .' WHERE '. '(COL2=\''. $imp3 .'\') and '. $case;
              
                  $get_id3= $this->db->query($combine3);
                  $get_id3_data=$get_id3->result_array();
                  
                  $get_id_data['id3']=$get_id3_data;
                  // print_r($get_id3_data);
                }
          
                

          } 


          return($get_id_data);
      }
}