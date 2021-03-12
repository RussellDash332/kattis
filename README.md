# RussellDash332/kattis ☕🐍💎
This repository is basically a tidier documentation of all my submissions to [Kattis](https://open.kattis.com/) (open version).
[NUS version](https://nus.kattis.com/) here.

### Small Notes
+ All JavaScript files will have names containing either one of "sm" and "node", depending on the runtime used ([SpiderMonkey](https://en.wikipedia.org/wiki/SpiderMonkey) or [Node.js](https://en.wikipedia.org/wiki/Node.js)). If the name doesn't contain any of the letters, then the code uses the SpiderMonkey runtime.
+ Regarding the templates
    + **Template.java** uses the classes [BufferedReader](https://docs.oracle.com/javase/8/docs/api/java/io/BufferedReader.html) and [PrintWriter](https://docs.oracle.com/javase/8/docs/api/java/io/PrintWriter.html) which is generally faster than using the [Scanner](https://docs.oracle.com/javase/8/docs/api/java/util/Scanner.html) class.
    + **Template2.java** uses the Reader class, which is very very fast for integer/long inputs. Otherwise, like for string inputs, use **Template.java**, which handles them better.
    + **template.cpp** is a much better, efficient, and faster version than **template-old.cpp**, I will use the former from now on.

That's all for now. 😊
> NB: Can you guess what the three logos on the header stand for?