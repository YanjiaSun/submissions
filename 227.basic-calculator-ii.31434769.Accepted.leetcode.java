  public class Solution
  {
    Stack<Integer> numStack = new Stack<Integer>();
    Stack<Character> opStack = new Stack<Character>();

    public int calculate(String s)
    {
      if (s == null || s.length() == 0)
      {
        return 0;
      }

      int i = 0;

      while (i < s.length())
      {
        char c = s.charAt(i);

        if (c >= '0' && c <= '9')
        {
          int num = 0;

          while (i < s.length() && s.charAt(i) >= '0' && s.charAt(i) <= '9')
          {
            num = num * 10 + (int) (s.charAt(i) - '0');
            i++ ;
          }

          pushNum(num);
          i-- ;
        }
        else if (c != ' ')
        {
          pushOp(c);
        }

        i++ ;
      }

      if (!opStack.isEmpty())
      {
        int right = numStack.pop();
        int left = numStack.pop();
        char lastOp = opStack.pop();
        numStack.push(cal(left, right, lastOp));
      }

      return numStack.pop();
    }

    private int cal(int left, int right, char op)
    {
      switch (op)
      {
        case '+':
          return left + right;

        case '-':
          return left - right;

        case '*':
          return left * right;

        case '/':
          return left / right;

        default:
          return 0;
      }
    }

    private void pushNum(int num)
    {
      if (numStack.isEmpty())
      {
        numStack.push(num);
      }
      else
      {
        char op = opStack.peek();

        if (op == '*' || op == '/')
        {
          opStack.pop();
          int last = numStack.pop();
          numStack.push(cal(last, num, op));
        }
        else
        {
          numStack.push(num);
        }
      }
    }

    private void pushOp(char op)
    {
      if (opStack.isEmpty() || op == '*' || op == '/')
      {
        opStack.push(op);
      }
      else
      {
        int right = numStack.pop();
        int left = numStack.pop();
        char lastOp = opStack.pop();
        numStack.push(cal(left, right, lastOp));
        opStack.push(op);
      }
    }
  }

