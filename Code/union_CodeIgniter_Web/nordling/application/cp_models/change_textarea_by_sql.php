<?php 

class change_textarea_by_sql extends CI_Model{

      public function get_data($data){            
          
          $rand =$data['rand'];
          $this->load->database();
   
          $str ="SELECT * FROM gd_range5 WHERE COL1 = '";
          for($i=0;$i<count($data)-4;$i++){
             $name= 'name_' .$i ; 
             if($i!=(count($data)-5)){
              $str .= $data[$name]. "'or COL1 = '";
             }else{
              $str .= $data[$name]."'";
             }

          }

          $get_id= $this->db->query($str);
          $get_id_data=$get_id->result_array();
          
		            $sql_name=str_replace('S970', 'S', $data['sql']);
		            // 篩選  X Y 最大值
		            $string_sql_x ='';
		            $string_sql_y ='';

                for($i=0;$i<count($get_id_data);$i++){
                  	for($j=0;$j<count($data)-4;$j++){
                       $name= 'name_' .$j ; 
                       if($get_id_data[$i]['COL1'] == $data[$name]){
          	             $id           = $get_id_data[$i]['COL1'];
          	             $get_sql      = $this->db->query("SELECT * FROM $sql_name WHERE COL1 = '$id'");
                         $get_sql_data = $get_sql->result_array();
                         if(!empty($get_sql_data[0]['COL5'])){ 
                         $str =$data['text1']-1;
                         $end =$data['text2']-$data['text1']+1;
                         $exp =explode(',',$get_sql_data[0]['COL5']);

                         if($end<explode("..", $get_sql_data[0]['COL3'])[1]){
                         $sli =array_slice($exp , $str ,$end);
                         }else{
                         $sli =array_slice($exp , $str ,explode("..", $get_sql_data[0]['COL3'])[1]); 
                         }
                         $id_data=implode(',',$sli);

                         $sql_gene[$j]['data']= $id_data;
                         $sql_gene[$j]['sql']  = $sql_name ; 
                         $sql_gene[$j]['rand']  = $rand  ;
                         $sql_gene[$j]['id']  = $id ;
                         $sql_gene[$j]['cut']  = $get_sql_data[0]['COL4'];
                         $sql_gene[$j]['len']  = $get_sql_data[0]['COL3'];
                         $sql_gene[$j]['max_x_str']=$data['text1'];
                         $sql_gene[$j]['max_x_end']=$data['text2'];
                         
                         $sql_gene[$j]['name'] = $get_id_data[$i]['COL2'];
                         $sql_gene[$j]['jpg']  = $id.'_'.$sql_name.'_'.$rand.'_gene_page1.jpg';  

                         
                         $string_sql_y  .= ','.$id_data;                           
                }else{
                     $get_sql     = $this->db->query("SELECT * FROM gd_range5 WHERE COL1 = '$id'");
                          $get_sql_data  = $get_sql->result_array();
       
                           $sql_gene[$j]['data']="NO";
                         $sql_gene[$j]['sql']  = $sql_name ; 
                         $sql_gene[$j]['rand']  = $rand  ;
                         $sql_gene[$j]['id']  = $id ;
                         $sql_gene[$j]['cut']  = $get_sql_data[0]['COL4'];
                         $sql_gene[$j]['len']  = $get_sql_data[0]['COL3'];
                         $sql_gene[$j]['max_x_str']=$data['text1'];
                         $sql_gene[$j]['max_x_end']=$data['text2'];
                         
                         $sql_gene[$j]['name'] = $get_id_data[$i]['COL2'];
                         $sql_gene[$j]['jpg']  = $id.'_'.$sql_name.'_'.$rand.'_gene_page1.jpg';  

                         

                }} }
                    }
                for($i=0;$i<count($get_id_data);$i++){
                  	
          	           
                         
                         $sql_gene[$i]['max_x']=$data['text2'];
                         $sql_gene[$i]['max_y']=max(explode(',',  $string_sql_y));
                 
          }
 
        return $sql_gene ;
      }
}