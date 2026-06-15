---
title: "The Beginner’s JavaScript Cheat Sheet (Download for Free)"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "javascript-cheat-sheet"
url: "https://www.semrush.com/blog/javascript-cheat-sheet/"
canonical: "https://www.semrush.com/blog/javascript-cheat-sheet/"
author: "Tushar Pol, Christine Skopec, Connor Lahey"
published: "2021-09-02T16:46:00+00:00"
updated: "2023-12-28T16:14:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2023_aging"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T17:08:43+00:00"
status_code: 200
html_hash: "cf13050fc268a45c4e8ab4239d62d66214709021539c826f5aab11934c787008"
clean_word_count: 7335
clean_char_count: 47139
---
# The Beginner’s JavaScript Cheat Sheet (Download for Free)

Ready to learn JavaScript quickly?

If yes, then you need this JavaScript cheat sheet. It covers the basics of JavaScript in a clear, concise, and beginner-friendly way.

Use it as a reference or a guide to improve your JavaScript skills.

Let’s dive in.

## What Is JavaScript?

JavaScript (JS) is a programming language primarily used for web development.

It allows developers to add interactivity and dynamic behavior to websites.

For example, you can use JavaScript to create interactive forms that validate users’ inputs in real time. Making error messages pop up as soon as users make mistakes.

Like this:

![An interactive sign-in form on Semrush](https://static.semrush.com/blog/uploads/media/be/e5/bee50657569be917bdb3ed47c4fb5b87/94a7f971021cef789e782619b7729f50/HR0tEgOu91t69BY0v_9rXN5kud5FlbvPlCSd5YKTgwjvosNbqMiHiFr_-tQ2VNcmifLH48RDueutCJ97irWZcaaSClUqdoln3t79q6Vbx7UQ6-KPmkBhwBBxMRoxC_8RvfVL_x4ouFuadGZ-97kRDq4.png)

JavaScript can also be used to enable features like accordions that expand and collapse content sections.

Here’s one example with the “SEO” section expanded:

![“SEO” section expanded on Semrush's site](https://static.semrush.com/blog/uploads/media/5d/ec/5dec1c833064c8a03a5a32c66cbe0ccf/c07f846884cf6616a174d7e0f6da33c3/kHJC6oW80GsY2kY6oOjTs5UeeN1wjGKNzZd05e6pFuDDbuEsKCpoDf-eTk7EPzfMMivgfz9onRr7sAlAVK4Q0lHP9mEzZp-8z4dInVFPx2bJ5yhGrkXDyrtCa1FOfT2kz9GxUh4Z5Ho95ifBHl_0HBY.png)

In the example above, clicking on each element in the series shows different content.

JavaScript makes this possible by manipulating the HTML and CSS of the page in real time.

JavaScript is also extremely useful in web-based applications like Gmail.

When you receive new emails in your Gmail inbox, JavaScript is responsible for updating the inbox and notifying you of new messages without the need for manually refreshing.

![New emails in Gmail inbox](https://static.semrush.com/blog/uploads/media/92/40/9240eee518fd4971144e8e7fb6edae34/c77c90d1e17d63c1582422170892067d/Smj71MztghAxnQotyaUKDcl-J2bGgoEIPvkC6ClxBnZ8HlrSKEGclsp8atAnDSBUM8G8v7FsY1hWS6kG0uH_i3vmUif8Wi9KkGvN8NSLflVIv7_yd4WbJCukeG7gJs9UgKg5_tTQkBOC4QlrzpC5XgE.png)

So, in other words:

JavaScript empowers web developers to craft rich user experiences on the internet.

## Understanding the Code Structure

To leverage JavaScript effectively, it's crucial to understand its code structure.

JavaScript code often sits in your webpages’ HTML.

It’s embedded using the <script> tags.

`<script>
// Your JavaScript code goes here
</script>`

You can also link to external JavaScript files using the src attribute within the <script> tag.

This approach is preferred for larger JavaScript codebases. Because it keeps your HTML clean and separates the code logic from the page content.

`<script src="mycode.js"></script>`

Now, let's explore the essential components that you can use in your JavaScript code.

## List of JavaScript Components (Cheat Sheet Included)

Below, you’ll find the most essential components used in JavaScript.

As you become more familiar with these building blocks, you'll have the tools to create engaging and user-friendly websites.

(Here’s the [cheat sheet](https://static.semrush.com/blog/uploads/files/ed/16/ed16dcde31055dcbe662137fd04f09f7/javascript-cheat-sheet.pdf), which you can download and keep as a handy reference for all these components. )

### Variables

Variables are containers that store some value. That value can be of any data type, such as strings (meaning text) or numbers.

There are three keywords for declaring (i.e., creating) variables in JavaScript: “var,” “let,” and “const.”

#### var Keyword

“var” is a keyword used to tell JavaScript to make a new variable.

After we make a variable with “var,” it works like a container to store things.

Consider the following example.

`var name = "Adam";`

Here, we’ve created a variable called “name” and put the value “Adam” in it.

This value is usable. Meaning we can use the variable "name" to get the value "Adam" whenever we need it in our code.

For example, we can write:

`var name = "Adam";
console.log("Hello, " + name);`

This means the second line will show “Hello, Adam” in your console (a message window for checking the output of your program).

Values in the variables created using the keyword var can be changed. You can modify them later in your code.

Here’s an example to illustrate this point:

`var name = "Adam";
name = "John";
console.log("Hello, " + name);`

First, we’ve put “Adam” in the “name” variable. Later, we changed the value of the same variable to “John.” This means that when we run this program, the output we will see in the console is “Hello, John.”

But, remember one thing:

In modern JavaScript, people often prefer using “let” and “const” keywords (more on those in a moment) over “var.” Because “let” and “const” provide [improved scoping rules](https://www.freecodecamp.org/news/var-let-and-const-whats-the-difference/).

#### let Keyword

An alternative to “var,” “let” is another keyword for creating variables in JavaScript.

Like this:

`let name = "Adam";`

Now, we can use the variable “name” in our program to show the value it stores.

For example:

`let name = "Adam";
console.log("Hello, " + name);`

This program will display "Hello, Adam" in the console when you run it.

If you want to override the value your variable stores, you can do that like this:

`var name = "Adam";
name = "Steve";
console.log("Hello, " + name);`

#### const Keyword

“const” is similar to “let,” but declares a fixed variable.

Which means:

Once you enter a value in it, you can't change it later.

Using “const” for things like numeric values helps prevent bugs by avoiding unintended changes later in code.

“const” also makes the intent clear. Other developers can see at a glance which variables are meant to remain unchanged.

For example:

`let name = "Adam";
const age = 30;`

Using “const” for "age" in this example helps prevent unintentional changes to a person's age.

It also makes it clear to other developers that "age" is meant to remain constant throughout the code.

### Operators

Operators are symbols that perform operations on variables.

Imagine you have some numbers and you want to do math with them, like adding, subtracting, or comparing them.

In JavaScript, we use special symbols to do this, and these are called operators. The main types of operators are:

#### Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations on numbers. These include:

|  |  |  |
| --- | --- | --- |
| **Operator Name** | **Symbol** | **Description** |
| “Addition” operator | + | The “addition” operator adds numbers together |
| “Subtraction” operator | - | The “subtraction” operator subtracts the right-hand value from the left-hand value |
| “Multiplication” operator | \* | The “multiplication” operator multiplies numbers together |
| “Division” operator | / | The “division” operator divides the left-hand number by the right-hand number |
| “Modulus” operator | % | The “modulus” operator returns a remainder after division |

Let’s put all of these operators to use and write a basic program:

`let a = 10;
let b = 3;
let c = a + b;
console.log("c");
let d = a - b;
console.log("d");
let e = a * b;
console.log("e");
let f = a / b;
console.log("f");
let g = a % b;
console.log("g");`

Here's what this program does:

- It sets two variables, “a” and “b,” to 10 and 3, respectively
- Then, it uses the arithmetic operators:
  - “+” to add the value of “a” and “b”
  - “-” to subtract the value of “b” from “a”
  - “\*” to multiply the value of “a” and “b”
  - “/” to divide the value of “a” by “b”
  - “%” to find the remainder when “a” is divided by “b”
- It displays the results of each arithmetic operation using “console.log()”

#### Comparison Operators

Comparison operators compare two values and return a boolean result—i.e., either true or false.

They’re essential for writing conditional logic in JavaScript.

The main comparison operators are:

|  |  |  |
| --- | --- | --- |
| **Operator Name** | **Symbol** | **Description** |
| “Equality” operator | == | Compares if two values are equal, regardless of data type. For example, “5 == 5.0” would return “true” even though the first value is an integer and the other is a floating-point number (a numeric value with decimal places) with the same numeric value. |
| “Strict equality” operator | === | Compares if two values are equal, including the data type. For example, “5 === 5.0” would return “false” because the first value is an integer and the other is a floating-point number, which is a different data type. |
| “Inequality” operator | != | Checks if two values are not equal. It doesn’t matter what type of values they are. For example, “5 != 10” would return “true” because 5 does not equal 10. |
| “Strict inequality” operator | !== | Checks if two values are not equal, including the data type. For example, “5 !== 5.0” would return “true” because the first value is an integer and the other is a floating-point number, which is a different data type. |
| “Greater than” operator | > | Checks if the left value is greater than the right value. For example, “10 > 5” returns “true.” |
| “Less than” operator | < | Checks if the left value is less than the right value. For example, “5 < 10” returns “true.” |
| “Greater than or equal to” operator | >= | Checks if the left value is greater than or equal to the right value. For example, “10 >= 5” returns “true.” |
| “Less than or equal to” operator | <= | Checks if the left value is less than or equal to the right value. For example, “5 <= 10” returns “true.” |

Let’s use all these operators and write a basic JS program to better understand how they work:

`let a = 5;
let b = 5.0;
let c = 10;
if (a == b) {
console.log('true');
} else {
console.log('false');
}
if (a === b) {
console.log('true');
} else {
console.log('false');
}
if (a != c) {
console.log('true');
} else {
console.log('false');
}
if (a !== b) {
console.log('true');
} else {
console.log('false');
}
if (c > a) {
console.log('true');
} else {
console.log('false');
}
if (a < c) {
console.log('true');
} else {
console.log('false');
}
if (c >= a) {
console.log('true');
} else {
console.log('false');
}
if (a <= c) {
console.log('true');
} else {
console.log('false');
}`

Here’s what this program does:

- It sets three variables: “a” with a value of 5, “b” with a value of 5.0 (a floating-point number), and “c” with a value of 10
- It uses the “==” operator to compare “a” and “b.” Since “a” and “b” have the same numeric value (5), it returns "true."
- It uses the “===” operator to compare “a” and “b.” This time, it checks not only the value but also the data type. Although the values are the same, “a” is an integer and “b” is a floating-point number. So, it returns "false."
- It uses the “!=” operator to compare “a” and “c.” As “a” and “c” have different values, it returns "true."
- It uses the “!==” operator to compare “a” and “b.” Again, it considers the data type, and since “a” and “b” are of different types (integer and floating-point), it returns "true."
- It uses the “>” operator to compare “c” and “a.” Since “c” is greater than “a,” it returns "true."
- It uses the “<” operator to compare “a” and “c.” As “a” is indeed less than “c,” it returns "true."
- It uses the “>=” operator to compare “c” and “a.” Since c is greater than or equal to a, it returns "true."
- It uses the “<=” operator to compare “a” and “c.” As “a” is less than or equal to “c,” it returns "true."

In short, this program uses the various comparison operators to make decisions based on the values of variables “a,” “b,” and “c.”

You can see how each operator compares these values and determines whether the conditions specified in the if statements are met. Leading to different console outputs.

#### Logical Operators

Logical operators allow you to perform logical operations with values.

These operators are typically used to make decisions in your code, control program flow, and create conditions for executing specific blocks of code.

There are three main logical operators in JavaScript:

|  |  |  |
| --- | --- | --- |
| **Operator Name** | **Symbol** | **Description** |
| “Logical AND” operator | && | The “logical AND” operator is used to combine two or more conditions. It returns “true” only if all the conditions are true. |
| “Logical OR” operator | | | | The “logical OR” operator is used to combine multiple conditions. And it returns “true” if at least one of the conditions is true. If all conditions are false, the result will be “false.” |
| “Logical NOT” operator | ! | The “logical NOT” operator is used to reverse the logical state of a single condition. If a condition is true, “!” makes it “false.” And if a condition is false, “!” makes it “true.” |

To better understand each of these operators, let’s consider the examples below.

First, a “&&” (logical AND) operator example:

`let age = 25;
let hasDriverLicense = true;
if (age >= 18 && hasDriverLicense) {
console.log("You can drive!");
} else {
console.log("You cannot drive.");
}`

In this example, the code checks if the age is greater than or equal to 18 and if the person has a driver's license. Since both conditions are true, its output is "You can drive!"

Second, a “| |” (logical OR) operator example:

`let isSunny = true;
let isWarm = true;
if (isSunny || isWarm) {
console.log("It's a great day!");
} else {
console.log("Not a great day.");
}`

In this example, the code outputs "It's a great day!" because one or both of the conditions hold true.

And third, a “!” (logical NOT) operator example:

`let isRaining = true;
if (!isRaining) {
console.log("It's not raining. You can go outside!");
} else {
console.log("It's raining. Stay indoors.");
}`

Here, the “!” operator inverts the value of isRaining from true to false.

So, the “if” condition “!isRaining” evaluates to false. Which means the code in the else block runs, returning "It's raining. Stay indoors."

#### Assignment Operators:

Assignment operators are used to assign values to variables. The standard assignment operator is the equals sign (=). But there are other options as well.

Here’s the complete list:

|  |  |  |
| --- | --- | --- |
| **Operator Name** | **Symbol** | **Description** |
| “Basic assignment” operator | = | The “basic assignment” operator is used to assign a value to a variable |
| “Addition assignment” operator | += | This operator adds a value to the variable's current value and assigns the result to the variable |
| “Subtraction assignment” operator | -= | This operator subtracts a value from the variable's current value and assigns the result to the variable |
| “Multiplication assignment” operator | \*= | This operator multiplies the variable's current value by a specified value and assigns the result to the variable |
| “Division assignment” operator | /= | This operator divides the variable's current value by a specified value and assigns the result to the variable |

Let’s understand these operators with the help of some code:

`let x = 10;
x += 5;
console.log("After addition: x = ", x);
x -= 3;
console.log("After subtraction: x = ", x);
x *= 4;
console.log("After multiplication: x = ", x);
x /= 6;
console.log("After division: x = ", x);`

In the code above, we create a variable called “x” and set it equal to 10. Then, we use various assignment operators to modify its value:

- “x += 5;” adds 5 to the current value of “x” and assigns the result back to “x.” So, after this operation, “x” becomes 15.
- “x -= 3;” subtracts 3 from the current value of “x” and assigns the result back to “x.” After this operation, “x” becomes 12.
- “x \*= 4;” multiplies the current value of “x” by 4 and assigns the result back to “x.” So, “x” becomes 48.
- “x /= 6;” divides the current value of “x” by 6 and assigns the result back to “x.” After this operation, “x” becomes 8.

At each operation, the code prints the updated values of “x” to the console.

### if-else

The “if-else” statement is a conditional statement that allows you to execute different blocks of code based on a condition.

It’s used to make decisions in your code by specifying what should happen when a particular condition is true. And what should happen when it’s false.

Here's an example to illustrate how “if-else” works:

`let age = 21;
if (age >= 18) {
console.log("You are an adult.");
} else {
console.log("You are a minor.");`

In this example, the “age” variable is compared to 18 using the “>=” operator.

Since “age >= 18” is true, the message "You are an adult." is displayed. But if it weren’t, the message "You are a minor." would’ve been displayed.

### Loops

Loops are programming constructs that allow you to repeatedly execute a block of code as long as a specified condition is met.

They’re essential for automating repetitive tasks.

JavaScript provides several types of loops, including:

#### for Loop

A “for” loop is a loop that specifies "do this a specific number of times."

It's well-structured and has three essential components: initialization, condition, and increment. This makes it a powerful tool for executing a block of code a predetermined number of times.

Here's the basic structure of a “for” loop:

`for (initialization; condition; increment) {
// Code to be executed as long as the condition is true
}`

The loop starts with the initialization (this is where you set up the loop by giving it a starting point), then checks the condition, and executes the code block if the condition is true.

After each iteration, the increment is applied, and the condition is checked again.

The loop ends when the condition becomes false.

For example, if you want to count from 1 to 10 using a “for” loop, here’s how you would do it:

`for (let i = 1; i <= 10; i++) {
console.log(i);
}`

In this example:

- The initialization part sets up a variable “i” to start at 1
- The loop keeps running as long as the condition (in this case, “i <= 10”) is true
- Inside the loop, it logs the value of “i” using “console.log(i)”
- After each run of the loop, the increment part, “i++”, adds 1 to the value of “i”

Here's what the output will look like when you run this code:

`1
2
3
4
5
6
7
8
9
10`

As you can see, the “for” loop starts with “i” at 1. And incrementally increases it by 1 in each iteration.

It continues until “i” reaches 10 because the condition “i <= 10” is satisfied.

The “console.log(i)” statement prints the current value of “i” during each iteration. And that results in the numbers from 1 to 10 being displayed in the console.

#### while Loop

A “while” loop is a loop that indicates "keep doing this as long as something is true."

It's a bit different from the “for” loop because it doesn't have an initialization, condition, and increment all bundled together. Instead, you write the condition and then put your code block inside the loop.

For example, if you want to count from 1 to 10 using a “while” loop, here’s how you would do it:

`let i = 1;
while (i <= 10) {
console.log(i);
i++;
}`

In this example:

- You initialize “i” to 1
- The loop keeps running as long as “i” is less than or equal to 10
- Inside the loop, it logs the value of “i” using “console.log(i)”
- “i” incrementally increases by 1 after each run of the loop

The output of this code will be:

`1
2
3
4
5
6
7
8
9
10`

So, with both “for” and “while” loops, you have the tools to repeat tasks and automate your code

#### do…while Loop

A “do...while” loop works similarly to “for” and “while” loops, but it has a different syntax.

Here's an example of counting from 1 to 10 using a “do...while” loop:

`let i = 1;
do {
console.log(i);
i++;
} while (i <= 10);`

In this example:

- You initialize the variable "i" to 1 before the loop starts
- The “do...while” loop begins by executing the code block, which logs the value of "i" using “console.log(i)”
- After each run of the loop, "i" incrementally increases by 1 using “i++”
- The loop continues to run as long as the condition "i <= 10" is true

The output of this code will be the same as in the previous examples:

`1
2
3
4
5
6
7
8
9
10`

#### for…in Loop

The “for...in” loop is used to iterate over the properties of an object (a data structure that holds key-value pairs).

It's particularly handy when you want to go through all the keys or properties of an object and perform an operation on each of them.

Here's the basic structure of a “for...in” loop:

`for (variable in object) {
// Code to be executed for each property
}`

And here’s an example of a “for...in” loop in action:

`const person = {
name: "Alice",
age: 30,
city: "New York"
};
for (let key in person) {
console.log(key, person[key]);
}`

In this example:

- You have an object named “person” with the properties “name,” “age,” and “city”
- The “for...in” loop iterates over the keys (in this case, "name," "age," and "city") of the “person” object
- Inside the loop, it logs both the property name (key) and its corresponding value in the “person” object

The output of this code will be:

`name Alice
age 30
city New York`

The “for...in” loop is a powerful tool when you want to perform tasks like data extraction or manipulation.

### Functions

A function is a block of code that performs a particular action in your code. Some common functions in JavaScript are:

#### alert() Function

This function displays a message in a pop-up dialog box in the browser. It's often used for simple notifications, error messages, or getting the user's attention.

Take a look at this sample code:

`alert("Hello, world!");`

When you call this function, it opens a small pop-up dialog box in the browser with the message “Hello, world!” And a user can acknowledge this message by clicking an "OK" button.

#### prompt() Function

This function displays a dialog box where the user can enter an input. The input is returned as a string.

Here’s an example:

`let name = prompt("Please enter your name: ");
console.log("Hello, " + name + "!");`

In this code, the user is asked to enter their name. And the value they provide is stored in the name variable.

Later, the code uses the name to greet the user by displaying a message, such as "Hello, [user's name]!"

#### confirm() Function

This function shows a confirmation dialog box with "OK" and "Cancel" buttons. It returns “true” if the user clicks "OK" and “false” if they click "Cancel."

Let’s illustrate with some sample code:

`const isConfirmed = confirm("Are you sure you want to continue?");
if (isConfirmed) {
console.log("true");
} else {
console.log("false");
}`

When this code is executed, the dialog box with the message "Are you sure you want to continue?" is displayed, and the user is presented with "OK" and "Cancel" buttons.

The user can click either the "OK" or "Cancel" button to make their choice.

The “confirm()” function then returns a boolean value (“true” or “false”) based on the user's choice: “true” if they click "OK" and “false” if they click "Cancel."

#### console.log() Function

This function is used to output messages and data to the browser's console.

Sample code:

`console.log("This is the output.");`

You probably recognize it from all our code examples from earlier in this post.

#### parseInt() Function

This function extracts and returns an integer from a string.

Sample code:

`const stringNumber = "42";
const integerNumber = parseInt(stringNumber);`

In this example, the “parseInt()” function processes the string and extracts the number 42.

The extracted integer is then stored in the variable “integerNumber.” Which you can use for various mathematical calculations.

#### parseFloat() Function

This function extracts and returns a floating-point number (a numeric value with decimal places).

Sample code:

`const stringNumber = "3.14";
const floatNumber = parseFloat(stringNumber);`

In the example above, the “parseFloat()” function processes the string and extracts the floating-point number 3.14.

The extracted floating-point number is then stored in the variable “floatNumber.”

### Strings

A string is a data type used to represent text.

It contains a sequence of characters, such as letters, numbers, symbols, and whitespace. Which are typically enclosed within double quotation marks (" ").

Here are some examples of strings in JavaScript:

`const name = "Alice";
const number = "82859888432";
const address = "123 Main St.";`

There are a lot of methods you can use to manipulate strings in JS code. These are most common ones:

#### toUpperCase() Method

This method converts all characters in a string to uppercase.

Example:

`let text = "Hello, World!";
let uppercase = text.toUpperCase();
console.log(uppercase);`

In this example, the “toUpperCase()” method processes the text string and converts all characters to uppercase.

As a result, the entire string becomes uppercase.

The converted string is then stored in the variable uppercase, and the output in your console is "HELLO, WORLD!"

#### toLowerCase() Method

This method converts all characters in a string to lowercase

Here’s an example:

`let text = "Hello, World!";
let lowercase = text.toLowerCase();
console.log(lowercase);`

After this code runs, the “lowercase” variable will contain the value "hello, world!" Which will then be the output in your console.

#### concat() Method

The “concat()” method is used to combine two or more strings and create a new string that contains the merged text.

It does not modify the original strings. Instead, it returns a new string that results from the combination of the original strings (called the concatenation).

Here's how it works:

`const string1 = "Hello, ";
const string2 = "world!";
const concatenatedString = string1.concat(string2);
console.log(concatenatedString);`

In this example, we have two strings, “string1” and “string2.” Which we want to concatenate.

We use the “concat()” method on “string1” and provide “string2” as an argument (an input value within the parentheses). The method combines the two strings and creates a new string, stored in the “concatenatedString” variable.

The program then outputs the end result to your console. In this case, that’s “Hello, world!”

#### match() Method

The “match()” method is used to search a string for a specified pattern and return the matches as an array (a data structure that holds a collection of values—like matched substrings or patterns).

It uses a regular expression for that. (A regular expression is a sequence of characters that defines a search pattern.)

The “match()” method is extremely useful for tasks like data extraction or pattern validation.

Here’s a sample code that uses the “match()” method:

`const text = "The quick brown fox jumps over the lazy dog";
const regex = /[A-Za-z]+/g;
const matches = text.match(regex);
console.log(matches);`

In this example, we have a string named “text.”

Then, we use the “match()” method on the “text” string and provide a regular expression as an argument.

This regular expression, “/[A-Za-z]+/g,” does two things:

1. It matches any letter from “A” to “Z,” regardless of whether it's uppercase or lowercase
2. It executes a global search (indicated by “g” at the end of the regular expression). This means the search doesn't stop after the first match is found. Instead, it continues to search through the entire string and returns all matches.

After that, all the matches are stored in the “matches” variable.

The program then outputs these matches to your console. In this case, it will be an array of all the words in the sentence "The quick brown fox jumps over the lazy dog."

#### charAt() Method

The “charAt()” method is used to retrieve the character at a specified index (position) within a string.

The first character is considered to be at index 0, the second character is at index 1, and so on.

Here’s an example:

`const text = "Hello, world!";
const character = text.charAt(7);
console.log(character);`

In this example, we have the string “text,” and we use the “charAt()” method to access the character at index 7.

The result is the character "w" because "w" is at position 7 within the string.

#### replace() Method

The “replace()” method is used to search for a specified substring (a part within a string) and replace it with another substring.

It specifies both the substring you want to search for and the substring you want to replace it with.

Here's how it works:

`const text = "Hello, world!";
const newtext = text.replace("world", "there");
console.log(newtext);`

In this example, we use the “replace()” method to search for the substring "world" and replace it with "there."

The result is a new string (“newtext”) that contains the replaced text. Meaning the output is, “Hello, there!”

#### substr() Method

The “substr()” method is used to extract a portion of a string, starting from a specified index and extending for a specified number of characters.

It specifies the starting index from which you want to begin extracting characters and the number of characters to extract.

Here's how it works:

`const text = "Hello, world!";
const substring = text.substr(7, 5);
console.log(substring);`

In this example, we use the “substr()” method to start extracting characters from index 7 (which is “w”) and continue for five characters.

The output is the substring "world."

(Note that the first character is always considered to be at index 0. And you start counting from there on.)

### Events

Events are actions that happen in the browser, such as a user clicking a button, a webpage finishing loading, or an element on the page being hovered over with a mouse.

Understanding these is essential for creating interactive and dynamic webpages. Because they allow you to respond to user actions and execute code accordingly.

Here are the most common events supported by JavaScript:

#### onclick Event

The “onclick” event executes a function or script when an HTML element (such as a button or a link) is clicked by a user.

Here’s the code implementation for this event:

`<button id="myButton" onclick="changeText()">Click me</button>
<script>
function changeText() {
let button = document.getElementById("myButton");
button.textContent = "Clicked!";
}
</script>`

Now, let's understand how this code works:

- When the HTML page loads, it displays a button with the text "Click me"
- When a user clicks on the button, the “onclick” attribute specified in the HTML tells the browser to call the “changeText” function
- The “changeText” function is executed and selects the button element using its id ("myButton")
- The “textContent” property of the button changes to "Clicked!"

As a result, when the button is clicked, its text changes from "Click me" to "Clicked!"

It's a simple example of adding interactivity to a webpage using JavaScript.

#### onmouseover Event

The “onmouseover” event occurs when a user moves the mouse pointer over an HTML element, such as an image, a button, or a hyperlink.

Here’s how the code that executes this event looks:

`<img id="myImage" src="image.jpg" onmouseover="showMessage()">
<script>
function showMessage() {
alert("Mouse over the image!");
}
</script>`

In this example, we have an HTML image element with the “id” attribute set to "myImage."

It also has an “onmouseover” attribute specified, which indicates that when the user hovers the mouse pointer over the image, the "showMessage ()" function should be executed.

This function displays an alert dialog with the message "Mouse over the image!"

The “onmouseover” event is useful for adding interactivity to your web pages. Such as providing tooltips, changing the appearance of elements, or triggering actions when the mouse moves over specific areas of the page.

#### onkeyup Event

The “onkeyup” is an event that occurs when a user releases a key on their keyboard after pressing it.

Here’s the code implementation for this event:

`<input type="text" id="myInput" onkeyup="handleKeyUp()">
<script>
function handleKeyUp() {
let input = document.getElementById("myInput");
let userInput = input.value;
console.log("User input: " + userInput);
}
</script>`

In this example, we have an HTML text input element <input> with the “id” attribute set to "myInput."

It also has an “onkeyup” attribute specified, indicating that when a key is released inside the input field, the "handleKeyUp()" function should be executed.

Then, when the user types or releases a key in the input field, the “handleKeyUp()” function is called.

The function retrieves the input value from the text field and logs it to the console.

This event is commonly used in forms and text input fields to respond to a user’s input in real time.

It’s helpful for tasks like auto-suggestions and character counting, as it allows you to capture users’ keyboard inputs as they type.

#### onmouseout Event

The “onmouseout” event occurs when a user moves the mouse pointer out of the area occupied by an HTML element like an image, a button, or a hyperlink.

When the event is triggered, a predefined function or script is executed.

Here’s an example:

`<img id="myImage" src="image.jpg" onmouseout="hideMessage()">
<script>
function hideMessage() {
alert("Mouse left the image area!");
}
</script>`

In this example, we have an HTML image element with the “id” attribute set to "myImage."

It also has an “onmouseout” attribute specified, indicating that when the user moves the mouse cursor out of the image area, the "hideMessage()" function should be executed.

Then, when the user moves the mouse cursor out of the image area, a JavaScript function called “hideMessage()” is called.

The function displays an alert dialog with the message "Mouse left the image area!"

#### onload Event

The “onload” event executes a function or script when a webpage or a specific element within the page (such as an image or a frame) has finished loading.

Here’s the code implementation for this event:

`<body onload="initializePage()">
<script>
function initializePage() {
alert("Page has finished loading!");
}
</script>`

In this example, when the webpage has fully loaded, the “initializePage()” function is executed, and an alert with the message "Page has finished loading!" is displayed.

#### onfocus Event

The “onfocus” event triggers when an HTML element like an input field receives focus or becomes the active element of a user’s input or interaction.

Take a look at this sample code:

`<input type="text" id="myInput" onfocus="handleFocus()">
<script>
function handleFocus() {
alert("Input field has received focus!");
}
</script>`

In this example, we have an HTML text input element <input> with the “id” attribute set to "myInput."

It also has an “onfocus” attribute specified. Which indicates that when the user clicks on the input field or tabs into it, the "handleFocus()" function will be executed.

This function displays an alert with the message "Input field has received focus!"

The “onfocus” event is commonly used in web forms to provide visual cues (like changing the background color or displaying additional information) to users when they interact with input fields.

#### onsubmit Event

The “onsubmit” event triggers when a user submits an HTML form. Typically by clicking a "Submit" button or pressing the "Enter" key within a form field.

It allows you to define a function or script that should be executed when the user attempts to submit the form.

Here’s a code sample:

`<form id="myForm" onsubmit="handleSubmit()">
<input type="text" name="username" placeholder="Username">
<input type="password" name="password" placeholder="Password">
<button type="submit">Submit</button>
</form>
<script>
function handleSubmit() {
let form = document.getElementById("myForm");
alert("Form submitted!");
}
</script>`

In this example, we have an HTML form element with the “id” attribute set to "myForm."

It also has an “onsubmit” attribute specified, which triggers the "handleSubmit()" function when a user submits the form.

This function shows an alert with the message "Form submitted!"

### Numbers and Math

JavaScript supports lots of methods (pre-defined functions) to deal with numbers and do mathematical calculations.

Some of the methods it supports include:

#### Math.abs() Method

This method returns the absolute value of a number, ensuring the result is positive.

Here's an example that demonstrates the use of the “Math.abs()” method:

`let negativeNumber = -5;
let positiveNumber = Math.abs(negativeNumber);
console.log("Absolute value of -5 is: " + positiveNumber);`

In this code, we start with a negative number (-5). By applying “Math.abs(),” we obtain the absolute (positive) value of 5.

This method is helpful for scenarios where you need to ensure that a value is non-negative, regardless of its initial sign.

#### Math.round() Method

This method rounds a number up to the nearest integer.

Sample code:

`let decimalNumber = 3.61;
let roundedUpNumber = Math.round(decimalNumber);
console.log("Ceiling of 3.61 is: " + roundedUpNumber);`

In this code, we have a decimal number (3.61). Applying “Math.round()” rounds it up to the nearest integer. Which is 4.

This method is commonly used in scenarios when you want to round up quantities, such as when calculating the number of items needed for a particular task or when dealing with quantities that can't be fractional.

#### Math.max() Method

This method returns the largest value among the provided numbers or values. You can pass multiple arguments to find the maximum value.

Here's an example that demonstrates the use of the “Math.max()” method:

`let maxValue = Math.max(5, 8, 12, 7, 20, -3);
console.log("The maximum value is: " + maxValue);`

In this code, we pass several numbers as arguments to the “Math.max()” method.

The method then returns the largest value from the provided set of numbers, which is 20 in this case.

This method is commonly used in scenarios like finding the highest score in a game or the maximum temperature in a set of data points.

#### Math.min() Method

The “Math.min()” method returns the smallest value among the provided numbers or values.

Sample code:

`let minValue = Math.min(5, 8, 12, 7, 20, -3);
console.log("The minimum value is: " + minValue);`

In this code, we pass several numbers as arguments to the “Math.min()” method.

The method then returns the smallest value from the given set of numbers, which is -3.

This method is commonly used in situations like identifying the shortest distance between multiple points on a map or finding the lowest temperature in a set of data points.

#### Math.random() Method

This method generates a random floating-point number between 0 (inclusive) and 1 (exclusive).

Here’s some sample code:

`const randomValue = Math.random();
console.log("Random value between 0 and 1: " + randomValue);`

In this code, we call the “Math.random()” method, which returns a random value between 0 (inclusive) and 1 (exclusive).

It's often used in applications where randomness is required.

#### Math.pow() Method

This method calculates the value of a base raised to the power of an exponent.

Let’s look at an example:

`` let base = 2;
let exponent = 3;
let result = Math.pow(base, exponent);
console.log(`${base}^${exponent} is equal to: ${result}`) ``

In this code, we have a base value of 2 and an exponent value of 3. By applying “Math.pow(),” we calculate 2 raised to the power of 3, which is 8.

#### Math.sqrt() Method

This method computes the square root of a number.

Take a look at this sample code:

`` let number = 16;
const squareRoot = Math.sqrt(number);
console.log(`The square root of ${number} is: ${squareRoot}`); ``

In this code, we have the number 16. By applying “Math.sqrt(),” we calculate the square root of 16. Which is 4.

#### Number.isInteger() Method

This method checks whether a given value is an integer. It returns true if the value is an integer and false if not.

Here's an example that demonstrates the use of the “Number.isInteger()” method:

`` let value1 = 42;
let value2 = 3.14;
let isInteger1 = Number.isInteger(value1);
let isInteger2 = Number.isInteger(value2);
console.log(`Is ${value1} an integer? ${isInteger1}`);
console.log(`Is ${value2} an integer? ${isInteger2}`); ``

In this code, we have two values, “value1” and “value2.” We use the “Number.isInteger()” method to check whether each value is an integer:

- For “value1” (42), “Number.isInteger()” returns “true” because it's an integer
- For “value2” (3.14), “Number.isInteger()” returns “false” because it's not an integer—it contains a fraction

### Date Objects

Date objects are used to work with dates and times.

They allow you to create, manipulate, and format date and time values in your JavaScript code.

Some common methods include:

#### getDate() Method

This method retrieves the current day of the month. The day is returned as an integer, ranging from 1 to 31.

Here's how you can use the “getDate()” method:

`` let currentDate = new Date();
let dayOfMonth = currentDate.getDate();
console.log(`Day of the month: ${dayOfMonth}`); ``

In this example, “currentDate” is a “date” object representing the current date and time.

We then use the “getDate()” method to retrieve the day of the month and store it in the “dayOfMonth” variable.

Finally, we display the day of the month using “console.log().”

#### getDay() Method

This method retrieves the current day of the week.

The day is returned as an integer, with Sunday being 0, Monday being 1, and so on. Up to Saturday being 6.

Sample code:

`` let currentDate = new Date();
let dayOfWeek = currentDate.getDay();
console.log(`Day of the week: ${dayOfWeek}`); ``

Here, “currentDate” is a date object representing the current date and time.

We then use the “getDay()” method to retrieve the day of the week and store it in the “dayOfWeek” variable.

Finally, we display the day of the week using “console.log().”

#### getMinutes()Method

This method retrieves the minutes portion from the present date and time.

The minutes will be an integer value, ranging from 0 to 59.

Sample code:

`` let currentDate = new Date();
let minutes = currentDate.getMinutes();
console.log(`Minutes: ${minutes}`); ``

In this example, “currentDate” is a “date” object representing the current date and time.

We use the “getMinutes()” method to retrieve the minutes component and store it in the minutes variable.

Finally, we display the minutes using “console.log().”

#### getFullYear() Method

This method retrieves the current year. It’ll be a four-digit integer.

Here’s some sample code:

`` let currentDate = new Date();
let year = currentDate.getFullYear();
console.log(`Year: ${year}`); ``

Here, “currentDate” is a date object representing the current date and time.

We use the “getFullYear()” method to retrieve the year and store it in the year variable.

We then use “console.log()” to display the year.

#### setDate() Method

This method sets the day of the month. By changing the day of the month value within the “date” object.

Sample code:

`` let currentDate = new Date();
currentDate.setDate(15);
console.log(`Updated date: ${currentDate}`); ``

In this example, “currentDate” is a “date” object representing the current date and time.

We use the “setDate()” method to set the day of the month to 15. And the “date” object is updated accordingly.

Lastly, we display the updated date using “console.log().”

## How to Identify JavaScript Issues

JavaScript errors are common. And you should address them as soon as you can.

Even if your code is error-free, search engines may have trouble rendering your website content correctly. Which can prevent them from indexing your website properly.

As a result, your website may get less traffic and visibility.

You can check to see if JS is causing any rendering issues by auditing your website with Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) tool.

Open the tool and enter your website URL. Then, click “**Start Audit**.”

![Site Audit search bar](https://static.semrush.com/blog/uploads/media/02/49/024904268c279de4767378cb02344ba0/8850a217dc8613b16efbc0f0335aeabb/KewgxL-OkRNAhtauI3WzaWH5utMviDO1KiHYni3jrkrrk-SDaw93gnAIldj6zprrZ8G3DwOaQhHG26J9BHnQ84fkFUVZFesLeDI2bYS1K1dQ-FO7YpPzof0f9H9ryPBW-6_fz3Vvp1lkZ5uiOf1-b-Y.png)

A new window will pop up. Here, set the scope of your audit.

![Site Audit Settings pop-up window](https://static.semrush.com/blog/uploads/media/12/61/1261c5c993c0315e661b44ef5ea00a49/9dcee45569cb2e15d27ec3bc90c94d76/Qu0-FBjnSNAoaMZCUXrsrkaomWv86fwp_AqN4c9b4Cb3vZIGPI8eHLpHBNwfpdqLsGfC5ihgDV84OOvO4uR-CsBCibQ38VyZbNQBOeNHNYuAePRPzq0IfrPJ6eRms1h1Lxu8AMkwH35DRz4pA2On36E.png)

After that, go to “**Crawler settings**” and enable the “JS rendering” option. Then, click “**Start Site Audit**.”

![Configure crawler settings in Site Audit tool](https://static.semrush.com/blog/uploads/media/8b/05/8b0507ff3aa20cdd0bbcb2286206a2de/31813b49c697416c43a52c855e8083aa/_0M6e6nMGKO-7HwglIJOSOGBbgcZSR8FfBZN_Ipg0kSDtKb9Oo70nPoEHvogT-yxJrwWO2iOsfo0DP69R4NetUVM2t6PR3ZEj_gruIMQfzKtgZpC9IBph2hS0AUZfMBFRGYLhWQQ3gzOULwylb9bZbI.png)

The tool will start auditing your site. After the audit is complete, navigate to the “**JS Impact**” tab.

You’ll see whether certain elements (links, content, title, etc.) are rendered differently by the browser and the crawler.

!["JS Impact” dashboard](https://static.semrush.com/blog/uploads/media/67/12/671201688fce559526ae04a0d1a42859/228afa5b5e4d8b171af00120c7f5bc0e/ulxSq5ZZIQLRHiyTKtXe0DhOpLxCpvUElJR0vM91oeh7z7B6F7He6ypPUI3FpAO18ehqt1fBYGEEcFGw7boZuwbNofOOVkOAIhSciMfzFpuhE3BFYG3KBQ0sZA_eYtA_EG2sgyzN4vviTb9JzAtlmf4.png)

For your website to be optimized, you should aim to minimize the differences between the browser and the crawler versions of your webpages.

This will ensure that your website content is fully accessible and indexable by search engines .

To minimize the differences, you should follow the best practices for [JavaScript SEO](https://www.semrush.com/blog/javascript-seo/) and implement [server-side rendering](https://web.dev/articles/rendering-on-the-web#client-side-rendering-csr) (SSR).

Even [Google recommends](https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering) doing this.

Why?

Because SSR minimizes the disparities between the version of your webpages that browser and search engines see.

You can then rerun the audit to confirm that the issues are resolved.

## Get Started with JavaScript

Learning how to code in JavaScript is a skill. It’ll take time to master it.

Thankfully, we’ve put together a handy cheat sheet to help you learn the basics of JavaScript and get started with your coding journey.

You can [download the cheat sheet](https://static.semrush.com/blog/uploads/files/22/4b/224ba365b7998bf7b965b190d5b4895c/javascript-cheat-sheet.pdf) as a PDF file or view it online.

We hope this cheat sheet will help you get familiar with the JavaScript language. And boost your confidence and skills as a coder.
