<?php 

class text_by_id extends CI_Model{

    public function get_data($data){  

        $rand =$data['rand'];
        $this->load->database();

        $sql=['SRR970490','SRR970538','SRR970561','SRR970565','SRR970587','SRR970588','Ribo_N_Rep1','Ribo_N_Rep2','Ribo_H_Rep1','Ribo_H_Rep2'];
        // echo "<pre>";
        // print_r($data);
        $cou=0;
        for($i=1;$i<4;$i++){

            $ck = $i.'_ck';
            $site = $i-1;

            if(!empty($data[$ck][0])){
                       
               for($k=0;$k<count($data[$ck]);$k++){

                   $id           = $data[$ck][$k];
                   
                   $get_range= $this->db->query("SELECT * FROM gd_range5 WHERE COL1 = '$id'");
                   $get_range=$get_range->result_array();

                   $string_id_x  = "";
                   $string_id_y  = "";


                   $string_id_cut_x  = "";

                   //取出 XY 最大值 
                   for($j=0;$j<count($sql);$j++){
              
                       if(in_array($sql[$j], array_keys($data))){
                          $sql_name=str_replace('SRR970', 'S', $sql[$j]);
                          $get_sql        = $this->db->query("SELECT * FROM $sql_name WHERE COL1 = '$id'");
                          $get_sql_data   = $get_sql->result_array();
                          if(!empty($get_sql_data[0]['COL5'])){    

                             $string_id_x  .= '..'. $get_range[0]['COL3'];
                             $string_id_cut_x  .= '..'. $get_range[0]['COL4'];

                             $string_id_y  .= ',' . $get_sql_data[0]['COL5']; 

                          }
                       }
                   }

                   //畫圖
                   
                   for($j=0;$j<count($sql);$j++){

                       $sql_name=str_replace('SRR970', 'S', $sql[$j]);

                       if(in_array($sql[$j], array_keys($data))){

                          $get_sql        = $this->db->query("SELECT * FROM $sql_name WHERE COL1 = '$id'");
                          $get_sql_data   = $get_sql->result_array();
                          
                          if(!empty($get_sql_data[0]['COL5'])){ 

                          $id_sql[$sql_name][$cou]['sql']  = $sql_name ; 
                          $id_sql[$sql_name][$cou]['rand']  = $rand  ;
                          $id_sql[$sql_name][$cou]['max_x']= max(explode('..', $string_id_x));
                          $id_sql[$sql_name][$cou]['max_y']= max(explode(',',  $string_id_y)); 
                          $id_sql[$sql_name][$cou]['name'] = $data['mytext'][$site];
                          $id_sql[$sql_name][$cou]['id']   = $get_range[0]['COL1'];
                          $id_sql[$sql_name][$cou]['cut'] = $get_range[0]['COL4'];
                          $id_sql[$sql_name][$cou]['max_cut_x']= max(explode('..', $string_id_cut_x));
                          $id_sql[$sql_name][$cou]['len'] = $get_range[0]['COL3'];
                          $id_sql[$sql_name][$cou]['data']= $get_sql_data[0]['COL5'];
                          $id_sql[$sql_name][$cou]['jpg'] = $get_range[0]['COL1'].'_'.$sql_name.'_'.$rand.'_id_page2.jpg';
                          

                         //  $w            =$j+4;
                         // $co           ='COL' . $w ;
                 
                         // $get_express      = $this->db->query("SELECT $co FROM Express WHERE COL2 = '$id'");
                         // $get_express_data = $get_express->result_array();
                         
                         // if(!empty($get_express_data)){
                         //   $id_sql[$sql_name][$cou]['express']  = $get_express_data[0][$co];

                          
                         // }else{
                         //  $id_sql[$sql_name][$cou]['express']  = 0;
                           
                         // }
                          
                          $cou++;        
                          }else{
                         $get_sql     = $this->db->query("SELECT * FROM gd_range5 WHERE COL1 = '$id'");
                          $get_sql_data  = $get_sql->result_array();
                          // print_r($get_sql_data);
                          $id_sql[$sql_name][$cou]['sql']  = $sql_name ; 
                        $id_sql[$sql_name][$cou]['rand']  = $rand  ;
                        $id_sql[$sql_name][$cou]['max_x']= explode('..', $get_sql_data[0]['COL3'])[1];
                          $id_sql[$sql_name][$cou]['max_y']= max(explode(',',  $string_id_y)); 
                          $id_sql[$sql_name][$cou]['len'] = $get_range[0]['COL3'];
                          $id_sql[$sql_name][$cou]['name'] = $data['mytext'][$site];
                          $id_sql[$sql_name][$cou]['id']   = $get_range[0]['COL1'];
                          $id_sql[$sql_name][$cou]['cut'] = $get_range[0]['COL4'];
                          $id_sql[$sql_name][$cou]['max_cut_x']= max(explode('..', $string_id_cut_x));
                          $id_sql[$sql_name][$cou]['data']= "NO";
                          $id_sql[$sql_name][$cou]['jpg'] = $get_range[0]['COL1'].'_'.$sql_name.'_'.$rand.'_id_page2.jpg';

                         //  $w            =$j+4;
                         // $co           ='COL' . $w ;
                 
                         // $get_express      = $this->db->query("SELECT $co FROM Express WHERE COL2 = '$id'");
                         // $get_express_data = $get_express->result_array();
                         
                         // if(!empty($get_express_data)){
                         //   $id_sql[$sql_name][$cou]['express']  = $get_express_data[0][$co];

                          
                         // }else{
                         //  $id_sql[$sql_name][$cou]['express']  = 0;
                           
                         // }
                          
                          $cou++;        
                          }
                       }
                   }
                   
               }
            }       
        }  
        // print_r($id_sql);
        return $id_sql ;
    }
}

?>