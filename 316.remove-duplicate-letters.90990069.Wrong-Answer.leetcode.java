<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
public class Solution
{
    public String removeDuplicateLetters(String s)
    {
        Map<Character, Integer> counts = new HashMap<Character, Integer>();
        char[] chs = s.toCharArray();
        == == == =
            public class Solution
        {
            public String removeDuplicateLetters(String s)
            {
                Map<Character, Integer> counts = new HashMap<Character, Integer>();
                char[] chs = s.toCharArray();
                >>> >>> > Stashed changes

                for (char c : s.toCharArray())
                {
                    if (counts.get(c) == null)
                    {
                        counts.put(c, 0);
                    }

                    <<< <<< < Updated upstream
                    counts.put(c, counts.get(c) + 1);
                }

                Stack<Character> stack = new Stack<Character>();

                for (char c : chs)
                {
                    == == == =
                        counts.put(c, counts.get(c) + 1);
                }

                Stack<Character> stack = new Stack<Character>();

                for (char c : chs)
                {
                    >>> >>> > Stashed changes

                    if (stack.contains(c))
                    {
                        counts.put(c, counts.get(c) - 1);
                        continue;
                    }

                    <<< <<< < Updated upstream
                    == == == =
                        >>>>>>> Stashed changes

                        while (!stack.isEmpty() && stack.peek() > c && counts.get(stack.peek()) > 1)
                    {
                        stack.pop();
                    }

                    <<< <<< < Updated upstream
                    stack.push(c);
                }

                StringBuilder sb = new StringBuilder();
                == == == =
                    stack.push(c);
            }

            StringBuilder sb = new StringBuilder();

            >>> >>> > Stashed changes

            while (!stack.isEmpty())
            {
                sb.append(stack.pop());
            }

            <<< <<< < Updated upstream

            == == == =

                >>>>>>> Stashed changes
                return sb.reverse().toString();
        }
    }
    == == == =
        public class Solution
    {
        public String removeDuplicateLetters(String s)
        {
            Map<Character, Integer> counts = new HashMap<Character, Integer>();
            char[] chs = s.toCharArray();

            for (char c : s.toCharArray())
            {
                if (counts.get(c) == null)
                {
                    counts.put(c, 0);
                }

                counts.put(c, counts.get(c) + 1);
            }

            Stack<Character> stack = new Stack<Character>();

            for (char c : chs)
            {
                if (stack.contains(c))
                {
                    counts.put(c, counts.get(c) - 1);
                    continue;
                }

                while (!stack.isEmpty() && stack.peek() > c && counts.get(stack.peek()) > 1)
                {
                    stack.pop();
                }

                stack.push(c);
            }

            StringBuilder sb = new StringBuilder();

            while (!stack.isEmpty())
            {
                sb.append(stack.pop());
            }

            return sb.reverse().toString();
        }
    }
    >>> >>> > Stashed changes
    == == == =
        public class Solution
    {
        public String removeDuplicateLetters(String s)
        {
            Map<Character, Integer> counts = new HashMap<Character, Integer>();
            char[] chs = s.toCharArray();

            for (char c : s.toCharArray())
            {
                if (counts.get(c) == null)
                {
                    counts.put(c, 0);
                }

                counts.put(c, counts.get(c) + 1);
            }

            Stack<Character> stack = new Stack<Character>();

            for (char c : chs)
            {
                if (stack.contains(c))
                {
                    counts.put(c, counts.get(c) - 1);
                    continue;
                }

                while (!stack.isEmpty() && stack.peek() > c && counts.get(stack.peek()) > 1)
                {
                    stack.pop();
                }

                stack.push(c);
            }

            StringBuilder sb = new StringBuilder();

            while (!stack.isEmpty())
            {
                sb.append(stack.pop());
            }

            return sb.reverse().toString();
        }
    }
    >>> >>> > Stashed changes
    == == == =
        public class Solution
    {
        public String removeDuplicateLetters(String s)
        {
            Map<Character, Integer> counts = new HashMap<Character, Integer>();
            char[] chs = s.toCharArray();

            for (char c : s.toCharArray())
            {
                if (counts.get(c) == null)
                {
                    counts.put(c, 0);
                }

                counts.put(c, counts.get(c) + 1);
            }

            Stack<Character> stack = new Stack<Character>();

            for (char c : chs)
            {
                if (stack.contains(c))
                {
                    counts.put(c, counts.get(c) - 1);
                    continue;
                }

                while (!stack.isEmpty() && stack.peek() > c && counts.get(stack.peek()) > 1)
                {
                    stack.pop();
                }

                stack.push(c);
            }

            StringBuilder sb = new StringBuilder();

            while (!stack.isEmpty())
            {
                sb.append(stack.pop());
            }

            return sb.reverse().toString();
        }
    }
    >>> >>> > Stashed changes
    == == == =
        public class Solution
    {
        public String removeDuplicateLetters(String s)
        {
            Map<Character, Integer> counts = new HashMap<Character, Integer>();
            char[] chs = s.toCharArray();

            for (char c : s.toCharArray())
            {
                if (counts.get(c) == null)
                {
                    counts.put(c, 0);
                }

                counts.put(c, counts.get(c) + 1);
            }

            Stack<Character> stack = new Stack<Character>();

            for (char c : chs)
            {
                if (stack.contains(c))
                {
                    counts.put(c, counts.get(c) - 1);
                    continue;
                }

                while (!stack.isEmpty() && stack.peek() > c && counts.get(stack.peek()) > 1)
                {
                    stack.pop();
                }

                stack.push(c);
            }

            StringBuilder sb = new StringBuilder();

            while (!stack.isEmpty())
            {
                sb.append(stack.pop());
            }

            return sb.reverse().toString();
        }
    }
    >>> >>> > Stashed changes
    == == == =
        public class Solution
    {
        public String removeDuplicateLetters(String s)
        {
            Map<Character, Integer> counts = new HashMap<Character, Integer>();
            char[] chs = s.toCharArray();

            for (char c : s.toCharArray())
            {
                if (counts.get(c) == null)
                {
                    counts.put(c, 0);
                }

                counts.put(c, counts.get(c) + 1);
            }

            Stack<Character> stack = new Stack<Character>();

            for (char c : chs)
            {
                if (stack.contains(c))
                {
                    counts.put(c, counts.get(c) - 1);
                    continue;
                }

                while (!stack.isEmpty() && stack.peek() > c && counts.get(stack.peek()) > 1)
                {
                    stack.pop();
                }

                stack.push(c);
            }

            StringBuilder sb = new StringBuilder();

            while (!stack.isEmpty())
            {
                sb.append(stack.pop());
            }

            return sb.reverse().toString();
        }
    }
    >>> >>> > Stashed changes
    == == == =
        public class Solution
    {
        public String removeDuplicateLetters(String s)
        {
            Map<Character, Integer> counts = new HashMap<Character, Integer>();
            char[] chs = s.toCharArray();

            for (char c : s.toCharArray())
            {
                if (counts.get(c) == null)
                {
                    counts.put(c, 0);
                }

                counts.put(c, counts.get(c) + 1);
            }

            Stack<Character> stack = new Stack<Character>();

            for (char c : chs)
            {
                if (stack.contains(c))
                {
                    counts.put(c, counts.get(c) - 1);
                    continue;
                }

                while (!stack.isEmpty() && stack.peek() > c && counts.get(stack.peek()) > 1)
                {
                    stack.pop();
                }

                stack.push(c);
            }

            StringBuilder sb = new StringBuilder();

            while (!stack.isEmpty())
            {
                sb.append(stack.pop());
            }

            return sb.reverse().toString();
        }
    }
    >>> >>> > Stashed changes
    == == == =
        public class Solution
    {
        public String removeDuplicateLetters(String s)
        {
            Map<Character, Integer> counts = new HashMap<Character, Integer>();
            char[] chs = s.toCharArray();

            for (char c : s.toCharArray())
            {
                if (counts.get(c) == null)
                {
                    counts.put(c, 0);
                }

                counts.put(c, counts.get(c) + 1);
            }

            Stack<Character> stack = new Stack<Character>();

            for (char c : chs)
            {
                if (stack.contains(c))
                {
                    counts.put(c, counts.get(c) - 1);
                    continue;
                }

                while (!stack.isEmpty() && stack.peek() > c && counts.get(stack.peek()) > 1)
                {
                    stack.pop();
                }

                stack.push(c);
            }

            StringBuilder sb = new StringBuilder();

            while (!stack.isEmpty())
            {
                sb.append(stack.pop());
            }

            return sb.reverse().toString();
        }
    }
    >>> >>> > Stashed changes