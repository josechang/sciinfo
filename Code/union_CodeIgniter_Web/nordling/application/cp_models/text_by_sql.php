<?php 

class text_by_sql extends CI_Model{

    public function get_data($data){  

        $rand =$data['rand'];
        $this->load->database();

        $sql=['SRR970490','SRR970538','SRR970561','SRR970565','SRR970587','SRR970588','Ribo_N_Rep1','Ribo_N_Rep2','Ribo_H_Rep1','Ribo_H_Rep2'];
        // echo "<pre>";
        // print_r($data);
        //SQL
        for($j=0;$j<count($sql);$j++){
              
            if(in_array($sql[$j], array_keys($data))){

		       $sql_name=str_replace('SRR970', 'S', $sql[$j]);
                  
		       $string_sql_x  = "";
           $string_sql_y  = "";
           $string_small_x  = "";
           
          
                  
               //取 X Y 最大值
               for($k=1;$k<4;$k++){

                   $ck = $k.'_ck';

                   if(!empty($data[$ck][0])){
                       
                       for($i=0;$i<count($data[$ck]);$i++){
                     
                  	       $id             = $data[$ck][$i];
                           $get_range= $this->db->query("SELECT * FROM gd_range5 WHERE COL1 = '$id'");
                           $get_range=$get_range->result_array();
                           


          	               $get_sql        = $this->db->query("SELECT * FROM $sql_name WHERE COL1 = '$id'");
                           $get_sql_data   = $get_sql->result_array();
                           // echo "<pre>";
                           // print_r($get_sql_data);

                           $string_sql_x  .= '..'.$get_range[0]['COL3'];
                           $string_small_x  .= '..'.$get_range[0]['COL4'];
                           if(!empty($get_sql_data[0]['COL5'])){

                               
                               $string_sql_y  .= ',' .$get_sql_data[0]['COL5'];
                           }                                         
                       }
                   }
               }
               $max_x=max(explode('..', $string_sql_x));
               $max_y=max(explode(',', $string_sql_y));

               $max_cut_x=max(explode('..', $string_small_x));
               //畫圖

               $cou =0;
               for($k=1;$k<4;$k++){

                   $ck = $k.'_ck';
                   $site = $k-1;

                   if(!empty($data[$ck][0])){

                      for($i=0;$i<count($data[$ck]);$i++){                         
                     
                          $id             = $data[$ck][$i];
                          $get_range= $this->db->query("SELECT * FROM gd_range5 WHERE COL1 = '$id'");
                          $get_range=$get_range->result_array();

          	              $get_sql        = $this->db->query("SELECT * FROM $sql_name WHERE COL1 = '$id'");
                          $get_sql_data   = $get_sql->result_array();
                          
                          if(!empty($get_sql_data[0]['COL5'])){

                          $sql_id[$sql_name][$cou]['sql']  = $sql_name ; 
                          $sql_id[$sql_name][$cou]['rand']  = $rand  ;
                          $sql_id[$sql_name][$cou]['max_x']= $max_x;
                          $sql_id[$sql_name][$cou]['max_y']= $max_y; 
                          $sql_id[$sql_name][$cou]['name'] = $data['mytext'][$site];
                          $sql_id[$sql_name][$cou]['id']   = $get_range[0]['COL1'];
                          $sql_id[$sql_name][$cou]['cut'] = $get_range[0]['COL4'];
                          $sql_id[$sql_name][$cou]['max_cut_x']= $max_cut_x;
                          $sql_id[$sql_name][$cou]['len'] = $get_range[0]['COL3'];
                          $sql_id[$sql_name][$cou]['data']= $get_sql_data[0]['COL5'];
                          $sql_id[$sql_name][$cou]['jpg'] = $get_range[0]['COL1'].'_'.$sql_name.'_'.$rand.'_sql_page2.jpg';
                          
                         //表現亮先關閉
                         // $w            =$j+4;
                         // $co           ='COL' . $w ;
                 
                         // $get_express      = $this->db->query("SELECT $co FROM Express WHERE COL2 = '$id'");
                         // $get_express_data = $get_express->result_array();
                         
                         // if(!empty($get_express_data)){
                         //   $sql_id[$sql_name][$cou]['express']  = $get_express_data[0][$co];
                          
                         // }else{
                         //   $sql_id[$sql_name][$cou]['express']  = 0;
                           
                         // }
                          
                           $cou++; 
                          }
                         else{
                          $get_sql     = $this->db->query("SELECT * FROM gd_range5 WHERE COL1 = '$id'");
                          $get_sql_data  = $get_sql->result_array();
                          $sql_id[$sql_name][$cou]['sql']  = $sql_name ; 
                          $sql_id[$sql_name][$cou]['rand']  = $rand  ;
                          $sql_id[$sql_name][$cou]['max_x']= max(explode('..', $string_sql_x));
                          $sql_id[$sql_name][$cou]['max_y']= 0;
                          $sql_id[$sql_name][$cou]['name'] = $data['mytext'][$site];
                          $sql_id[$sql_name][$cou]['id']   = $get_range[0]['COL1'];
                          $sql_id[$sql_name][$cou]['cut'] = $get_range[0]['COL4'];
                          $sql_id[$sql_name][$cou]['max_cut_x']= $max_cut_x;
                          $sql_id[$sql_name][$cou]['len'] = $get_range[0]['COL3'];
                          $sql_id[$sql_name][$cou]['data']= "NO";
                          $sql_id[$sql_name][$cou]['jpg'] = $get_range[0]['COL1'].'_'.$sql_name.'_'.$rand.'_sql_page2.jpg';
                          

               //           $w            =$j+4;
               //           $co           ='COL' . $w ;
                 
               //           $get_express      = $this->db->query("SELECT $co FROM Express WHERE COL2 = '$id'");
               //           $get_express_data = $get_express->result_array();

               //            if(!empty($get_express_data)){
               //             $sql_id[$sql_name][$cou]['express']  = $get_express_data[0][$co];
                          
               //           }else{
               //             $sql_id[$sql_name][$cou]['express']  = 0;
                           
               //           }

                          $cou++; 


                          }               
                      }

                   }
               } 




            }
        } 
        // echo "1111111111"."<br>";
               // echo "<pre>";
               // print_r($sql_id);
      return $sql_id; 
      
    }
}

?>