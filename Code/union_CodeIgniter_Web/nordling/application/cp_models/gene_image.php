<?php 

class gene_image extends CI_Model{

      public function get_data($data){  

        // print_r($data);

        //$data['sql'] ==Ribo_N_vs_H  所以秀出四種資料庫
        $sql     = $data['sql']  ;
        $all_ribo = ["Ribo_H_Rep1","Ribo_H_Rep2","Ribo_N_Rep1","Ribo_N_Rep2"];
        $gene = $data['gene'] ;
        $this->load->database();
        
        $str="";
        $str1="";
        for($i=0;$i<count($all_ribo);$i++){

            $combine = 'SELECT * FROM '. $all_ribo[$i] .' WHERE COL2 = \''.$gene.'\'';
            $get_id= $this->db->query($combine);
            $get_id_data[$i]['data']=$get_id->result_array();
            $get_id_data[$i]['vs']  =$sql;
            $get_id_data[$i]['sql'] = $all_ribo[$i];
            for($j=0;$j<count($get_id_data[$i]['data']);$j++){
                $str .="..".$get_id_data[$i]['data'][$j]['COL3'];
                $str1 .="..".$get_id_data[$i]['data'][$j]['COL5'];
            }
            $ex_str =max(explode("..", $str));
            $ey_str =max(explode(",", $str1));
            $get_id_data[$i]['max_x'] =$ex_str;
            $get_id_data[$i]['max_y'] =$ey_str;

        }
        
        return($get_id_data);
      }
}
?>