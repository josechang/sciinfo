<?php 

class textarea_by_id extends CI_Model{

      public function get_data($data){ 

      // echo "<pre>";            
          // print_r($data);
          $rand =$data['rand'];
          $this->load->database();
          
          $ck = str_replace("\n","' or COL2 = '",$data['mytextarea']);
         
          $get_id= $this->db->query("SELECT * FROM gd_range5 WHERE COL2 = '$ck'");
          $get_id_data=$get_id->result_array();
          
          // print_r($get_id_data);
          $sql=['SRR970490','SRR970538','SRR970561','SRR970565','SRR970587','SRR970588'];


          for($i=0;$i<count($get_id_data);$i++){

             $id  = $get_id_data[$i]['COL1'];

             $string_id_x ='';
		     $string_id_y ='';
          $range=explode("..",$get_id_data[$i]['COL3'])[1];

                         
		      #ID 區分

		     // 篩選  X Y 最大值
          	 for($j=0;$j<count($sql);$j++){

	            if(in_array($sql[$j], array_keys($data))){

	            	 $sql_name     = str_replace('SRR970', 'S', $sql[$j]);
	            	     
          	         $get_sql      = $this->db->query("SELECT * FROM $sql_name WHERE COL1 = '$id'");
                     $get_sql_data = $get_sql->result_array();
                     $string_id_x  .= '..'.$range;

                     if(!empty($get_sql_data[0]['COL5'])){
                         $string_id_y  .= ','.$get_sql_data[0]['COL5'];  
                         }
                      
                }              
             }

             //畫圖
             for($j=0;$j<count($sql);$j++){

	            if(in_array($sql[$j], array_keys($data))){

	            	 $sql_name     = str_replace('SRR970', 'S', $sql[$j]);
	            	 
          	         $get_sql      = $this->db->query("SELECT * FROM $sql_name WHERE COL1 = '$id' ");
                     $get_sql_data = $get_sql->result_array();

                     $id_gene[$sql_name][$i]['max_x']=max(explode('..', $string_id_x));  
                     $id_gene[$sql_name][$i]['max_y']=max(explode(',',  $string_id_y));
                      $id_gene[$sql_name][$i]['rand']  = $rand  ;
                     $id_gene[$sql_name][$i]['name'] = $get_id_data[$i]['COL2'];
                     $id_gene[$sql_name][$i]['len']   = $get_id_data[$i]['COL3'];
                     $id_gene[$sql_name][$i]['cut'] = $get_id_data[$i]['COL4'];

                     if(!empty($get_sql_data[0]['COL5'])){
                         $id_gene[$sql_name][$i]['data']= $get_sql_data[0]['COL5'];
                         }else{
                         $id_gene[$sql_name][$i]['data'] = "NO" ;
                         }
                     $id_gene[$sql_name][$i]['id']   = $get_id_data[$i]['COL1'];
                     $id_gene[$sql_name][$i]['jpg'] = $get_id_data[$i]['COL1'].'_'.$sql_name.'_'.$rand.'_id_page1.jpg';
                     $id_gene[$sql_name][$i]['sql'] =$sql_name; 
                     
                }              
             }

             for($j=0;$j<count($sql);$j++){
                        
                    if(in_array($sql[$j], array_keys($data))){
                         $w            =$j+4;
                         $co           ='COL' . $w ;
                 
                         $get_express      = $this->db->query("SELECT $co FROM Express WHERE COL2 = '$id'");
                         $get_express_data = $get_express->result_array();
                         
                         if(!empty($get_express_data)){
                           $id_gene[$sql_name][$i]['express']  = $get_express_data[0][$co];

                          
                         }else{
                           $id_gene[$sql_name][$i]['express']  = 0;
                           
                         }
                        
                    }
                                                 
                  }
          }
          return $id_gene;
      }
}

?>         