import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 *
 */
public class Test {
    /**
     * 返回第n个罗马数字对应的阿拉伯数字
     *
     * @param n
     * @return
     */
    public static int getArab(int n) {
        // 1, 5, 10, 50, 100, 500, 1000,...
        if (n % 2 == 1) {
            return Double.valueOf(Math.pow(10, n / 2)).intValue();
        } else {
            return Double.valueOf(5 * Math.pow(10, n / 2 - 1)).intValue();
        }
    }

    /**
     * 判断当前阿拉伯数字可不可重复, 也就是判断是否是10的幂次方
     *
     * @param value
     * @return
     */
    public static boolean isRepeatableArabValue(int value) {
        return Double.valueOf(Math.log10(value)) == Double.valueOf(Math.log10(value)).intValue();
    }

    /**
     * 用一个Object来保存遍历过程中的各种状态
     */
    public static class Obj {
        // 罗马数字
        private String romanStr;

        // 是否是重复的罗马数字
        private boolean isRepeat;

        // 当前的阿拉伯数字
        private int curArabValue;

        //开始遍历的起始值
        private int startArabValue;

        // 保存重置过的值. 用于判断是否出现了死循环,如果出现了,代表输入值不能计算出结果,应该停止循环
        private List<Integer> resetValueList = new ArrayList<>();

        public Obj(String romanStr, boolean isRepeat) {
            this.romanStr = romanStr;
            this.isRepeat = isRepeat;
            this.startArabValue = 1;//不管可不可重复,都是从1开始
            this.curArabValue = startArabValue;
        }

        public void resetStartArabValue(int value) {
            if (value != 1 && resetValueList.contains(value)) {
                // 出现死循环,抛异常
                throw new RuntimeException("occur endless cycle");
            }
            this.startArabValue = value;
            this.curArabValue = startArabValue;

            // 如果出现重置为1的情况,所以更前面的值被重置了,所以需要清除循环列表,重新计算
            if (value == 1) {
                this.resetValueList.clear();
            }
            this.resetValueList.add(value);
        }

        public void resetArabValue() {
            this.curArabValue = startArabValue;
        }

        /**
         * 重设阿拉伯数字,往下遍历
         *
         * @return
         */
        public int getNextArabValue() {
            if (isRepeat) {
                curArabValue = 10 * curArabValue;
            } else {
                if (isRepeatableArabValue(curArabValue)) {
                    curArabValue = 5 * curArabValue;
                } else {
                    curArabValue = 2 * curArabValue;
                }
            }
            return curArabValue;
        }

        public boolean isCurArabValueRepeatable() {
            return isRepeatableArabValue(curArabValue);
        }

        public String getRomanStr() {
            return romanStr;
        }

        public boolean isRepeat() {
            return isRepeat;
        }

        public int getCurArabValue() {
            return curArabValue;
        }

        public int getStartArabValue() {
            return startArabValue;
        }

        public void setCurArabValue(int curArabValue) {
            this.curArabValue = curArabValue;
        }

        @Override
        public String toString() {
            return "Obj{" +
                    "romanStr='" + romanStr + '\'' +
                    ", isRepeat=" + isRepeat +
                    ", curArabValue=" + curArabValue +
                    ", startArabValue=" + startArabValue +
                    ", resetValueList=" + resetValueList +
                    '}';
        }
    }

    public static void main(String[] args) {
        //有结果的情况
        //test("AhZhJ"); //Sure! It is 691 using Ah_Z_J
        //test("XXXVVVIII"); // Sure! It is 333 using X_V_I
        //test("AZERTY"); // Sure! It is 444 using ZAREYT
        // test("ABCADDEFGF"); //Sure! It is 49269 using BA_C_DEF_G
        // test("MDCCLXXXVII");//Sure! It is 1787 using MDCLXVI
         // test("MDCCLXXXIX");//Sure! It is 1789 using MDCLX_I
         test("BCBC");
        // test("249");
        //test("MMMVII");//Sure! It is 37 using MVI
        //test("IV");//Sure! It is 4 using IV
        //test("ABCCDED");//Sure! It is 1719 using ABC_D_E
        //无结果的情况
        //test("0I"); // ask me something that's not impossible to do!
        //test("CCCC"); // ask me something that's not impossible to do!
        // test("ABAA"); // ask me something that's not impossible to do!
        // test("ABCDEFA"); // ask me something that's not impossible to do!
    }

    /**
     * 判断字符串中某个字符出现的次数
     *
     * @param str
     * @return
     */
    public static int CountCharNum(String source, String str) {
        int origialLength = source.length();
        String newStr = source.replace(str, "");
        return origialLength - newStr.length();
    }

    public static void test(String str) {
        // 1. 用正则表达式判断是否全是英文字母 并且不能连续重复4次
        if (!str.matches("[a-zA-Z]+") || str.matches("([a-zA-Z])\\1{3}")) {
            System.out.println("Hey, ask me something that's not impossible to do!");
            return;
        }

        String[] arr = str.split("");
        int len = arr.length;

        // 判断是否有重复数字
        List<Obj> objList = new ArrayList<>();
        for (int i = len - 1; i >= 0; i--) {
            boolean isRepeat = CountCharNum(str, arr[i]) > 1;
            Obj obj = new Obj(arr[i], isRepeat);
            objList.add(obj);
        }

        List<Integer> arabValueList;
        try {
            //获取阿拉伯数字列表
            arabValueList = getArabValueList(objList);
        } catch (Exception e) {
            //发生了死循环,没有结果
            System.out.println("Hey, ask me something that's not impossible to do!");
            return;
        }
        Map<Integer, String> romanSymbolMap = new HashMap<>();
        for (Obj obj : objList) {
            romanSymbolMap.put(obj.getCurArabValue(), obj.getRomanStr());
        }
        //计算当前最大的arab数字
        int curMaxArabValue = arabValueList.stream().max((v1, v2) -> v1 - v2).get();
        String romanSymbol = ""; // roman symbol
        int j = 1;
        while (true) {
            int arabValue = getArab(j);
            romanSymbol = String.join("", romanSymbolMap.containsKey(arabValue) ? romanSymbolMap.get(arabValue) : "_", romanSymbol);
            if (arabValue == curMaxArabValue) {
                break;
            }
            j++;
        }

        int sum = 0; // 阿拉伯数字求和
        for (int i = 0; i < arabValueList.size(); i++) {
            if (i == 0) {
                sum += arabValueList.get(i);
                continue;
            }
            if (arabValueList.get(i) < arabValueList.get(i - 1)) {
                sum -= arabValueList.get(i);
            } else {
                sum += arabValueList.get(i);
            }
        }
        System.out.println("Sure! It is " + sum + " using " + romanSymbol);
    }

    /**
     * 获取每个罗马数字对应的阿拉伯数字列表.
     *
     * @param objList
     * @return
     */
    public static List<Integer> getArabValueList(List<Obj> objList) {
        List<Integer> arabValueList = new ArrayList<>();

        Map<Integer, String> arab2RomanMap = new LinkedHashMap<>();
        Map<String, Integer> roman2ArabMap = new LinkedHashMap<>();

        //判断规则:
        //1. 对重复罗马字符的判断:
        //   (1). 要么全是+号.  比如69 = (10-1)+(50+10)
        //   (2). 要么第一个+,第二个-,但第一个+的右边是-. 比如149=(10-1)+(50-10)+100. 重复数字10,有加有减, 但仅限于第一个出现的10右边的数,要比10小
        //    错误情况: 151 = 1+50+100, 但不能拆分为1+10+(50-10)+100. 错误在于1+10+50-10不符合规则.
        // 2. 如果当前值是不可重复的,那么不能比左边的值小
        // 3. 除了左边一个值以外,当前值必须比更靠左边的值大(罗马字母不相等的情况下)
        // 4. 如果前一个值-, 当前值只能是+,不能连续-
        // 5.如果当前值比左边一个值小, 那么只能小两个位置. 比如说,可以100-10, 但不能100-1.

        //怎么保证最终的数字最小? 在满足规则的条件下,尽量减号越多越好.
        // 什么场景可以用减号: 可重复的数字,但并没有重复的情况下
        // 也就是说: 在遍历的过程中,如果发现, 你当前的操作是 一个可重复数字(实际没重复) + 不可重复数字.
        // 那么你应该往回倒推一步,变成不可重复数字-可重复数字.
        // 比如ABCD. 正常遍历的结果会是1+5+10+50, 也就是55. 但实际上, 你发现1,5满足一个不可重复数字+一个可重复数字(实际没重复),
        // 所以重新遍历,变成(5-1)+(50-10),得到44才是最小值

        // 如果发现某个条件不满足, 就重置不满足条件的罗马数字的变量起始点, 然后重新遍历
        // 如果判断没有结果的情况: 如果出现了死循环,就抛异常,判定没有结果.

        // 排序
        for (int i = 0; i < objList.size(); i++) {
            Obj curObj = objList.get(i);
            curObj.resetArabValue(); //每次重新遍历的时候,重置遍历起点
            int curArabValue = curObj.getCurArabValue();

            // 如果有相同的罗马数字, 取相同的值
            if (roman2ArabMap.containsKey(curObj.getRomanStr())) {
                curObj.setCurArabValue(roman2ArabMap.get(curObj.getRomanStr()));
                curArabValue = curObj.getCurArabValue();

                // 判断重复数字,要么全是+号, 要么(第一个+,第二个-,但第一个+的右边是-)
                boolean isRepeatValueNegative = curObj.isRepeat() && curObj.getCurArabValue() < objList.get(i - 1).getCurArabValue();

                if (isRepeatValueNegative) {
                    //需要回溯, 往回走, 找到第一个重复字符的位置
                    for (int ii = 0; ii < i; ii++) {
                        if (objList.get(ii).getRomanStr().equals(curObj.getRomanStr())) {
                            // 如果满足第一个+的右边是-, 正确
                            if (objList.get(ii).getCurArabValue() > objList.get(ii + 1).getCurArabValue()) {
                                break;
                            }
                            // 重置遍历起始值
                            objList.get(ii).resetStartArabValue(objList.get(ii).getNextArabValue());
                            for (int k = ii + 1; k < objList.size(); k++) {
                                objList.get(k).resetStartArabValue(1);
                            }
                            // 重新遍历
                            return getArabValueList(objList);
                        }
                    }
                }
            }

            // 判断当前阿拉伯数字是否已经被别人占用
            boolean isBeenUsed = arab2RomanMap.containsKey(curArabValue) && !arab2RomanMap.get(curArabValue).equals(curObj.getRomanStr());
            // 如果当前值是不可重复的,那么不能比左边的值小
            boolean isIllegal = i > 0 && curArabValue < arabValueList.get(i - 1) && !curObj.isCurArabValueRepeatable();
            if (isBeenUsed || isIllegal) {
                //重设当前罗马数字的遍历起点,重新遍历
                curObj.resetStartArabValue(curObj.getNextArabValue());
                return getArabValueList(objList);
            }

            if (i > 1) {
                for (int j = 0; j < i - 1; j++) {
                    // 除了左边一个值以外,当前值必须比更靠左边的值大(罗马字母不相等的情况下)
                    if (curArabValue < objList.get(j).getCurArabValue() || (curArabValue == objList.get(j).getCurArabValue() && !curObj
                            .getRomanStr().equals(objList.get(j).getRomanStr()))) {
                        //重设当前罗马数字的遍历起点,重新遍历
                        curObj.resetStartArabValue(curObj.getNextArabValue());
                        return getArabValueList(objList);
                    }
                }

                // 如果前一个值-, 当前值只能是+,不能连续-
                if (arabValueList.get(i - 1) < arabValueList.get(i - 2)) {
                    if (curArabValue < arabValueList.get(i - 1)) {
                        //重设当前罗马数字的遍历起点,重新遍历
                        curObj.resetStartArabValue(curObj.getNextArabValue());
                        return getArabValueList(objList);
                    }
                }
                // 如果当前值比左边一个值小, 那么只能小两个位置. 比如说,可以100-10, 但不能100-1.
                if (curArabValue < objList.get(i - 1).getCurArabValue() && objList.get(i - 1).getCurArabValue() / curArabValue > 10) {
                    //重设当前罗马数字的遍历起点,重新遍历
                    curObj.resetStartArabValue(curObj.getNextArabValue());
                    return getArabValueList(objList);
                }
            }

            //再判断一下当前的组合是否最小值
            if (i > 0 && !curObj.isRepeat() && !objList.get(i - 1).isRepeat() && String.valueOf(curArabValue).length() == String.valueOf(
                    objList.get(i - 1).getCurArabValue()).length()) {
                while (curArabValue > objList.get(i - 1).getCurArabValue()) {
                    //需要回溯到上一个值, 重新遍历
                    objList.get(i - 1).resetStartArabValue(objList.get(i - 1).getNextArabValue());
                    // 重新reset
                    for (int k = i; k < objList.size(); k++) {
                        objList.get(k).resetStartArabValue(1);
                    }
                    return getArabValueList(objList);
                }

            }
            arabValueList.add(curArabValue);
            arab2RomanMap.put(curArabValue, curObj.getRomanStr());
            roman2ArabMap.put(curObj.getRomanStr(), curArabValue);
        }
        return arabValueList;
    }
}