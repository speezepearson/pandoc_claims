Usage: just use `verify-claims.py` as a Pandoc filter:

        pandoc --filter=./verify-claims.py README.markdown -o README.html

Wrap any claim you make in a link, and give that link a `claim` attribute, which specifies a shell command to run to verify the claim:

* ``[`/dev/null` appears as an empty file.](){claim="test $(wc -c </dev/null) = 0"}``  
    appears as  
    [`/dev/null` appears as an empty file.](){claim="test $(wc -c </dev/null) = 0"}

* ``[`/` is the empty directory.](){claim="test $(ls / | wc -l) = 0"}``  
    appears as  
    [`/` is the empty directory.](){claim='test $(ls / | wc -l) = 0'}
