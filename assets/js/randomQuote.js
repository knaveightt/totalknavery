function getRandomQuote(file)
{
    var textContent;
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState == 4)
        {
            if(rawFile.status == 200 || rawFile.status == 0)
            {
                textContent = rawFile.responseText;
            }
        }
    }
    rawFile.send(null)

    var quotes = textContent.replace(/\n$/, '').split('\n');
    var quote = quotes[Math.floor(Math.random()*quotes.length)];
    return quote;
}
