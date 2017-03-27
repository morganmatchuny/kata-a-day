//Write a function called validBraces that 
//takes a string of braces, and determines 
//if the order of the braces is valid. 
//validBraces should return true if the 
//string is valid, and false if it's invalid.

function validBraces(braces) {
  const stack = []

  for(const brace of braces) {
    if (')]}'.includes(brace)) {
      if (isMatchedBraces(stack.pop(), brace)) {
        continue
      }
      return false
    }

    stack.push(brace)
  }

  return !stack.length
}

function isMatchedBraces(left, right) {
  return ['()', '[]', '{}'].some(([l, r]) => l === left && r === right)
}

module.exports = validBraces
