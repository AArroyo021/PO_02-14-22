package POWeekly;

public class Actualmemory {

    public static void main(String[] args) {
        System.out.println(actualMemorySize("32GB"));
        System.out.println(actualMemorySize("2GB"));
        System.out.println(actualMemorySize("512MB"));
        System.out.println(actualMemorySize("1GB"));
    }

    public static String actualMemorySize(String memory){
        String memoryString = memory.substring(0, memory.length()-2);
        double actualMemory = Double.parseDouble(memoryString) * 0.93;

        if(memory.endsWith("GB") && actualMemory > 1)
            return Math.round(actualMemory * 100.0)/ 100.0 + "GB";
        else if(memory.endsWith("GB") && actualMemory < 1)
           return (int)(actualMemory * 100) + "MB";
        else
            return (int)Math.round(actualMemory) + "MB";
    }
}
