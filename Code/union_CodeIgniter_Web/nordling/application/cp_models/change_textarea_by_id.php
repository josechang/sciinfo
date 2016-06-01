<?php  

class change_textarea_by_id extends CI_Model{

      public function get_data($data){ 

      echo "<pre>";            
          // print_r($data);
          $rand =$data['rand'];
          $this->load->database();
          
          $ck=$data['id'];
          $get_id= $this->db->query("SELECT * FROM gd_range5 WHERE COL1 = '$ck'");
          $get_id_data=$get_id->result_array();
          
          // print_r($get_id_data);
          $sql=['S970490','S970538','S970561','S970565','S970587','S970588'];


          // for($i=0;$i<count($get_id_data);$i++){

          //    $id  = $get_id_data[$i]['COL1'];

             $string_sql_x ='';
		         $string_sql_y ='';

		      #ID 區分

		     // // 篩選  X Y 最大值
          	 for($i=0;$i<count($data)-4;$i++){
                 $name="name_".$i;
                 $id  =$data['id'];
                 $sql_name    = str_replace('S970', 'S', $data[$name]);
	            // if(in_array($sql[$j], array_keys($data))){

	      //       	 $sql_name     = str_replace('SRR970', 'S', $sql[$j]);
	            	 
          	         $get_sql      = $this->db->query("SELECT * FROM $sql_name WHERE COL1 = '$id'");
                     $get_sql_data = $get_sql->result_array();
                     
                     if(!empty($get_sql_data[0]['COL5'])){ 
                     $str =$data['text1']-1;
                     $end =$data['text2']-$data['text1']+1;
                     $exp =explode(',',$get_sql_data[0]['COL5']);
                     $sli =array_slice($exp , $str ,$end);
                     $id_data=implode(',',$sli);
                     

                     $sql_gene[$i]['data'] =$id_data;
                     $sql_gene[$i]['sql']  = $sql_name ; 
                     $sql_gene[$i]['rand']  = $rand  ;
                     $sql_gene[$i]['id']  = $id ;
                     $sql_gene[$i]['cut']  = $get_sql_data[0]['COL4'];
                     $sql_gene[$i]['len']  = $get_sql_data[0]['COL3'];
                     $sql_gene[$i]['max_x_str']=$data['text1'];
                     $sql_gene[$i]['max_x_end']=$data['text2'];
                     $sql_gene[$i]['max_x']    =$data['text2']-$data['text1']+1;
                     $sql_gene[$i]['name'] = $get_id_data[0]['COL2'];
                     $sql_gene[$i]['jpg']  = $id.'_'.$sql_name.'_'.$rand.'_gene_page1.jpg';  

                     $string_sql_y  .= ','.$id_data;            
                }else{
                     $get_sql     = $this->db->query("SELECT * FROM gd_range5 WHERE COL1 = '$id'");
                          $get_sql_data  = $get_sql->result_array();
       
                           $sql_gene[$i]['sql']  = $sql_name ; 
                          $sql_gene[$i]['rand']  = $rand  ;
                          
                          $sql_gene[$i]['name'] = $get_sql_data[0]['COL2'];
                          $sql_gene[$i]['id']   = $get_sql_data[0]['COL1'];
                          $sql_gene[$i]['cut'] = $get_sql_data[0]['COL4'];
                          $sql_gene[$i]['len']  = $get_sql_data[0]['COL3'];
                          $sql_gene[$i]['data']= "NO";
                           $sql_gene[$i]['max_x_str']=$data['text1'];
                         $sql_gene[$i]['max_x_end']=$data['text2'];
                          $sql_gene[$i]['max_x']    =$data['text2']-$data['text1']+1;
                          $sql_gene[$i]['jpg'] = $get_sql_data[0]['COL1'].'_'.$sql_name.'_'.$rand.'_id_page2.jpg'; 

                }}             
             

                    
                for($i=0;$i<count($sql_gene);$i++){
                    
                       
                         

                         $sql_gene[$i]['max_y']=max(explode(',',  $string_sql_y));
                 
          }
    return $sql_gene;

       //       //畫圖
       //       for($j=0;$j<count($sql);$j++){

	      //       if(in_array($sql[$j], array_keys($data))){

	      //       	 $sql_name     = str_replace('SRR970', 'S', $sql[$j]);
	            	 
       //    	         $get_sql      = $this->db->query("SELECT * FROM $sql_name WHERE COL1 = '$id' ");
       //               $get_sql_data = $get_sql->result_array();

       //               $id_gene[$sql_name][$i]['max_x']=max(explode('..', $string_id_x));  
       //               $id_gene[$sql_name][$i]['max_y']=max(explode(',',  $string_id_y));
       //               $id_gene[$sql_name][$i]['rand']  = $rand  ;
       //               $id_gene[$sql_name][$i]['name'] = $get_id_data[$i]['COL2'];
       //               $id_gene[$sql_name][$i]['cut'] = $get_sql_data[0]['COL4'];
       //               $id_gene[$sql_name][$i]['data']= $get_sql_data[0]['COL5'];
       //               $id_gene[$sql_name][$i]['id']   = $get_sql_data[0]['COL1'];
       //               $id_gene[$sql_name][$i]['jpg'] = $get_sql_data[0]['COL1'].'_'.$sql_name.'_'.$rand.'_id_page1.jpg';
       //               $id_gene[$sql_name][$i]['sql'] =$sql_name; 
                     
       //          }              
       //       }
       //    }
       //    return $id_gene;
      }
}

?>         