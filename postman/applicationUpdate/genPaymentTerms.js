var totalTerms = 50
var pmt = 100
var pmtLast = 200
var arrayTerms = []
let currDate = new Date()
var startDate = currDate.toISOString().split('T')[0]
var date = startDate

// generate the array of terms
for (i = 0; i < totalTerms; i++){
    var year = parseInt(date.substring(0, 4))
    var month = parseInt(date.substring(5, 7))
    month %= 12

    // process year
    if (month == 0){
        year += 1
        var yearFormat = year.toString()
        date = yearFormat + date.substring(4, date.length)
    }
    // process month
    if (month < 9){
        month += 1
        var monthFormat = '0' + month.toString()
    }
    else{
        month += 1
        var monthFormat = month.toString()
    }

    date = date.substring(0, 5) + monthFormat + date.substring(7, date.length)
    
    // if the final term
    if (i == totalTerms-1){
        pmt = pmtLast
    }
    var object = {
        "paymentDate": date,
        "tenure": i+1,
        "pmt": pmt
    }
    
    arrayTerms.push(object);
}

var convert = JSON.stringify(arrayTerms)  // to JSON string


console.log(typeof(arrayTerms));
console.log(arrayTerms);
console.log(arrayTerms.length);

console.log(typeof(convert));
console.log(convert);
