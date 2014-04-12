import scala.annotation.tailrec

object CookieClickerAlpha {

  val BASE_COOKIES = 2;

  class CookieSolver {
    def cookie_solver(farm_cost: Double, extra_cookies: Double, win_num: Double): Double = {
      @tailrec
      def solve(time: Double, bases: Int, prev_time: Double): Double = {
        val base_time = win_num / (BASE_COOKIES + (bases * extra_cookies));
        val new_time = time + base_time;
        if (new_time < prev_time) {
          val _time = time + (farm_cost / (BASE_COOKIES + (bases * extra_cookies)));
          return solve(_time, bases + 1, new_time);
        } else {
          return prev_time;
        }
      }

      val bases = 0;
      val _time = (farm_cost / (BASE_COOKIES + (bases * extra_cookies)));
      return solve(_time, bases + 1, (win_num / BASE_COOKIES));
    }
  }

  def main(args: Array[String]) {
    val input = if (args.length < 1) io.Source.stdin
                else io.Source.fromFile(args(0));

    val cs = new CookieSolver();

    var case_num = 1;
    for (line <- input.getLines()) {
      val in = line.trim.split("""\s+""").map(x => x.toDouble);

      if (in.length > 1) {
        val Array(farm_cost, extra_cookies, win_num) = in.map(x => x.toDouble);
        val answer = cs.cookie_solver(farm_cost, extra_cookies, win_num);

        println("Case #%d: %.7f".format(case_num, answer));
        case_num = case_num + 1;
      }
    }
  }

}
