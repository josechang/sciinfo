<?php 

class sql_gene extends CI_Model{

    public function get($data){  

          $this->load->database();
          
          $sql_name=[];
          $Ribo=['Ribo_H_Rep1','Ribo_H_Rep2','Ribo_N_Rep1','Ribo_N_Rep2'];
          if(in_array('Ribo_N_vs_H',array_keys($data))){
          	 for($i=0;$i<count($Ribo);$i++){
               array_push($sql_name,$Ribo[$i]);
             }

          }      
          $gene = $data['gene'];


           
           $combine = 'SELECT * FROM '. 'Ribo_N_vs_H '.'WHERE COL1= \''. $gene .'\'';
           $get_id= $this->db->query($combine);
           $get_id_data=$get_id->result_array();
           $get_id_data['sql'] ='Ribo_N_vs_H';
           return($get_id_data);

    }
}
?>