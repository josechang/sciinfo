<?php 

class id_image extends CI_Model{

      public function get_data($data){  
        // print_r($data);
        $sql     = $data['sql']  ;
        $id      = $data['id']   ;
        $gene    = $data['gene'] ;

        $all_ribo = ["Ribo_H_Rep1","Ribo_H_Rep2","Ribo_N_Rep1","Ribo_N_Rep2"];
        $this->load->database();
        
        $str="";
        $str1="";
        for($i=0;$i<count($all_ribo);$i++){

            $combine = 'SELECT * FROM '. $all_ribo[$i] .' WHERE COL1 = \''.$id.'\'';
            $get_id= $this->db->query($combine);
            $get_id_data[$i]['data']=$get_id->result_array();
            // print_r($get_id_data);
            $get_id_data[$i]['vs']  =$sql;
            $get_id_data[$i]['sql'] = $all_ribo[$i];
            
            $str .="..".$get_id_data[0]['data'][0]['COL3'];
            $str1 .=",".$get_id_data[0]['data'][0]['COL5'];        

        }
        $ex_str =max(explode("..", $str));
        $ey_str =max(explode(",", $str1));
        $get_id_data['max_x'] =$ex_str;
        $get_id_data['max_y'] =$ey_str;
        // echo "<pre>";
        // print_r($get_id_data);
        return($get_id_data);
      }
}
?>