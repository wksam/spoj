process.stdin.resume();
process.stdin.setEncoding('utf8');

require("readline").createInterface({
    input: process.stdin,
    output: process.stdout
}).on("line", (input) => {
	if(input == "42") process.exit();
    console.log(input);
});