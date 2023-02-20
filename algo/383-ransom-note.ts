// https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4427/
function canConstruct(ransomNote: string, magazine: string): boolean {
  if (magazine.length < 1) {
    return false;
  }

  let dictArr = [...magazine];

  for (const c of ransomNote) {
    const index = dictArr.indexOf(c);
    // If a character is not in the magazine, we know we can't use it
    if (index < 0) return false;
    dictArr.splice(index, 1);
  }

  return true;
}
