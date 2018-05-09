import math

def square_root(a):
	"""Newton's method to approximate the square root of a

	a: double
	"""
	x = a / 2
	while True:
		y = (x + a/x) / 2
		if abs(y-x) < 0.000001:
			break
		x = y
	return x


def test_square_root():
	print('%s\t%s\t%s\t%s' % ('a', 'mysqrt(a)', 'math.sqrt(a)', 'diff'))

	print('%s\t%s\t%s\t%s' % ('-', '-'*len('mysqrt(a)'), '-'*len('math.sqrt(a)'), '-'*len('diff')))

	for i in range(1, 11, 1):
		target = i * 1.0
		mysqrt = square_root(target)
		math_sqrt = math.sqrt(target)
		diff = abs(mysqrt - math_sqrt)
		print('%.1f\t%.11f\t%.11f\t%.11f' % (target, mysqrt, math_sqrt, diff) )

if __name__ == '__main__':
	test_square_root()