# LIVE CODING!

Build a search function with the following behaviour:

### Requirements:

1. An async function that accepts a query string
2. Returns a filtered list of results from a (mock) async data source
3. Cache results in memory so repeated identical queries skip the data source
4. Handle these states:
    - Loading (awaitable — caller knows it’s async)
    - No results (empty list, not an error)
    - Error (optional if time permits — wrap in `try/except`)

### NOTES:
- Create a new branch and do all your changes there
- Commit and push your changes to your branch
- Create a PR to main with your changes
- Feel free to add, change, and move in directories anything on the repository 
