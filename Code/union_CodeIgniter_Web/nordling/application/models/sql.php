<?php 

class sql extends CI_Model{

    public function gene_level($data){  

          $case   = $data['method'].$data['method_math'].$data['method_number'];
          $method =$data['method'];
          for($i=0;$i<count($data['sql']);$i++){
              $combine = 'SELECT * FROM '. $data['sql'][$i] .' WHERE '. $case .' order by '.$method .' DESC';

              $get_id= $this->db->query($combine);
              $get_id_data=$get_id->result_array();
              $sql_name=$data['sql'][$i];
              $output[$i]['name']=$sql_name;
              $output[$i]['data']=$get_id_data;
          }

          return($output);
    }
    public function ribo_express($data){

          $case = 'SELECT * FROM Ribo_N_vs_H WHERE COL1= \''. $data .'\'';
          $get_id= $this->db->query($case);
          $get_id_data=$get_id->result_array();
          return($get_id_data);
    }

    public function gene_level_ribo_data($data){  

      $combine       = "SELECT * FROM Ribo WHERE Gene='". $data ."' order by Isoform DESC";
      $get_gene      = $this->db->query($combine);
      $get_gene_data = $get_gene->result_array();

      $Max_x_h1='0';
      $Max_x_h2='0';
      $Max_x_n1='0';
      $Max_x_n2='0';

      


      for($i=0;$i<count($get_gene_data);$i++){
         $Max_y='0';
         $Max_x_h1 .= ",".explode("..",$get_gene_data[$i]['Length'])[1];
         $Max_x_h2 .= ",".explode("..",$get_gene_data[$i]['Length'])[1];
         $Max_x_n1 .= ",".explode("..",$get_gene_data[$i]['Length'])[1];
         $Max_x_n2 .= ",".explode("..",$get_gene_data[$i]['Length'])[1];

         $Max_y .= ",".$get_gene_data[$i]['Max_h1'];
         $Max_y .= ",".$get_gene_data[$i]['Max_h2'];
         $Max_y .= ",".$get_gene_data[$i]['Max_n1'];
         $Max_y .= ",".$get_gene_data[$i]['Max_n2'];
         $get_gene_data[$i]['Max_y']=$this->science->change(max(explode(',', $Max_y)));
      }

      $get_gene_data['Max_x_h1']=$this->science->change(max(explode(',', $Max_x_h1)));
      $get_gene_data['Max_x_h2']=$this->science->change(max(explode(',', $Max_x_h2)));
      $get_gene_data['Max_x_n1']=$this->science->change(max(explode(',', $Max_x_n1)));
      $get_gene_data['Max_x_n2']=$this->science->change(max(explode(',', $Max_x_n2)));

      return($get_gene_data);
    }

   
    public function gene_level_ribo_isoform($data){  

      $combine       = "SELECT * FROM new_ribo_H_vs_N_Isoform_Level WHERE Gene='". $data ."' order by Isoform DESC";
      $get_gene      = $this->db->query($combine);
      $get_gene_data =$get_gene->result_array();
      return($get_gene_data);
    }
}
?>