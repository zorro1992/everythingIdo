package com.raghu;

public class Main {

    public static void main(String[] args) {
        printMegaBytesAndKiloBytes(1025);
	// write your code here

    }
    public static void  printMegaBytesAndKiloBytes(int kiloBytes){
        if (kiloBytes == 0){
            System.out.println("Invalid Input");
        }
        else{
            int MB = (kiloBytes/1024);
            int KB = (kiloBytes % 1024);
            System.out.println(kiloBytes+" KB  = "+ MB +" MB "+ KB +" KB ");
        }
    }
}
