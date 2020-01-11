
//单行注释

/*
    多行注释
*/


/**
 *
 *  交换两个变量的值
 *
 * */

var num1 = 12;
var num2 = 34;

var temp;

temp = num1;
num1 = num2;
num2 = temp;


console.log(num1,num2);

/*
*
* 使用typeof关键字查看数据类型
* 基本数据类型包括了：number、string、boolean、undefined、null
* isNaN: 用来判断是否是一个数字，当返回true的时候说明是NaN，表示的不是一个数字，返回false，说明不是NaN，表示的是一个数字
*
* */

var a = 'abc';

console.log(isNaN(a));      //true
console.log(typeof(a));     //string



/*
*  不管是双引号，还是单引号，都是成对出现的(可以用单双引号混合使用)
*  引号非常多的时候,用转义字符:“\”
* */

console.log('我是"帅哥"'); // ==> 我是"帅哥"

console.log("我是'帅哥',\"哈哈哈\""); // ==> 我是'帅哥',"哈哈哈"



/*
*   两边只要有一个是字符串，那么+就是字符串拼接功能
*   两边如果都是数字，那么就是算术功能。
* */


console.log(11 + 11);             //  22
console.log("hello" + " world");  // "hello world"
console.log("100" + "100");       // "100100"
console.log("11" + 11);           // "1111"




/*
*   length属性用来获取字符串的长度
* */

var str = 'abcdefg';
str.length;     // 字符串的长度  10



/**
 *
 *  true和false，区分大小写(True，False不是布尔类型，只是标识符)
 *  NaN、""、undefined、null、alse、0 这6个值可以转换成false，其余的都是true
 *
 * */


/*
* undefined表示一个声明了没有赋值的变量
* */

var undefined_name ;
console.log(undefined_name); // undefined



/*
* null表示一个空的对象
* */

var null_name = null;
console.log(typeof null_name); // Object


/**
 *  undefiner值是派生自null值的，所以判断相等时为true，但是两种用途是完全不一样的
 *
 * */
/*
undefined == null;   // true
undefined === null;  // false
*/



