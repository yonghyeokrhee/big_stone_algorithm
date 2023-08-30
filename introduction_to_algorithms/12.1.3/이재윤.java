import java.util.*;

class Node{
    Node left;
    Node right;
    int val;
    
    public Node(int val){
        this.val = val; 
    }
}


public class Main {
    public static void main(String args[]) {
      
      Node node1 = new Node(1);
      Node node2 = new Node(2);
      Node node3 = new Node(3);
      Node node4 = new Node(4);
      Node node5 = new Node(5);
      
      node1.left = node2;
      node1.right = node3;
      node2.left = node4;
      node2.right = node5; 
      
      node3.left = null;
      node3.right = null;
      node4.left = null;
      node4.right = null;
      node5.left = null;
      node5.right = null;
      
      
      Stack<Node> stk = new Stack<>(); 
      Node root = node1; 
      stk.push(node1);
      int cnt = 0; 
      boolean[] visited = new boolean[10];
      
      
      
      while(true){
      
          if(cnt == 5){
              break;
          }    
          
          
          if(visited[root.val] == true){
              stk.pop();
              root = stk.peek();
              continue;
          }
          
          
          if(root.left == null && root.right == null){
              Node node = stk.pop();
              System.out.println(node.val);
              cnt += 1; 
              visited[node.val] = true;
              root = stk.peek();
              continue;
          }
          
          
          
          if(root.left != null & visited[root.left.val] == false){
              stk.push(root.left);
              root = root.left;
              continue; 
          }
          
          System.out.println(root.val);
          cnt += 1; 
          visited[root.val] = true; 
          
          if(root.right != null & visited[root.right.val] == false){
              stk.push(root.right);
              root = root.right; 
          }
          
          
          
          
          
          
      }
      
      
      
      
      
      
      
      
      
    }
}
