After a while, using the same methodologies we found another breach and the hash:
a7312e17ba07ab09dacfebc4cdc2fe516043c1c2fd71078abcebb1e2a017f6c8.
But they changed the way they process hashes.
Now each password in the db files contains a prefix with the number of times the password goes through hashing.
For example, for a password stored at pass_db3 that is written in the file like this: 
15_SAKDJNKJNASD - the hashing algorithm hashes the passwordFilename (first hashing, like previously), 
then hashes the result's hexdigets (2nd hashing), then the result's hexdigets (3rd hashing), until the 15th hashing. 
To verify you understand the algorithm you can use 4_examplePassword assuming it is stored in a file named examplepassdb.
