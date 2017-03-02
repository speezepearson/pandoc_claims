# About

In technical and scientific writing, it's respectable to support a document's claims by supplying evidence; often this evidence takes the form of computer code. For example, here are three claims that should be supported by evidence:

- "Our data shows an increasing trend in spray-cheese sales." 
    - *(What code revealed this increasing trend?)*
- "Our technique outperforms all others." 
    - *(What code did you run on your technique to conclude this?)*
- "In Linux, `/dev/null` appears an as empty file." 
    - *(What code demonstrates this?)*

This Pandoc filter helps by formatting text based on the success or failure of code tests that you associate with the text. 

# Examples


The following examples use `verify-claims.py` as a Pandoc filter at the command line:

        $ pandoc --filter=./verify-claims.py README.markdown -o README.html

## Example 1

Pandoc renders the Markdown text

    [Our technique outperforms all others.](){.claim cmd="./check-we-are-the-best.sh"}

as 

![](Images/success.png)

or

![](Images/failure.png),

depending on whether the program `check-we-are-the-best.sh` completes with exit value `0` (success) or nonzero (failure).


## Example 2


The (true) claim "The file `/dev/null` contains 0 characters" would be written in Markdown as

    [The file `/dev/null` contains 0 characters.](){.claim cmd="test $(wc -c </dev/null) = 0"}

and rendered normally:

![](Images/null0.png)

However, the opposite (false) statement "The file `/dev/null` is non-empty" would be written in Markdown

    [The file `/dev/null` is non-empty.](){.claim cmd="test $(wc -c </dev/null) -ne 0"}

and render with a strikethrough indicating its falsehood:

![](Images/null1.png)



## Example 3

The file `state-median-home-prices.csv` contains the median home price in $USD for each state in the U.S. for 2016:

    128969 AL
    241750 AK
    147669 AZ
    120560 AR
    ...

Consider the folowing claims: 

- "Hawaii has the highest median home prices of any state."
- "The median home price in Hawaii exceeds $450,000."
- "The median home price in Hawaii exceeds $500,000."


You can link the data to the claims by writing your claims in Markdown like this:

    ["Hawaii has the highest median home prices of any state."](){.claim cmd="test $(cat Examples/state-median-home-prices.csv | sort -n | tail -n 1 | cut -d' ' -f 2) = 'HI'"}

    ["The median home price in Hawaii exceeds $450,000."](){.claim cmd="test $(cat Examples/state-median-home-prices.csv | sort -n | tail -n 1 | cut -d" " -f 1) -gt 450000"}

    ["The median home price in Hawaii exceeds $500,000."](){.claim cmd="test $(cat Examples/state-median-home-prices.csv | sort -n | tail -n 1 | cut -d" " -f 1) -gt 500000"}

Pandoc renders this as

![](Images/home-prices.png)

so it is readily apparent that the last claim is not supported by the data.


