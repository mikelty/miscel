#TODO: 29.4, 107, 7 took too long

def calc_interest(本金,还钱总数,周期数,err_rate=1e-6):
	# 误差在本金*err_rate之内
	本额等息 = 还钱总数 / 周期数
	def get_err(本金, 周期利率):
		周期利率 /= 100.0  # 年化利率=年化利率/100.0
		剩余本金 = 本金
		for _ in range(周期数):
			本金 = 剩余本金 * (1 + 周期利率)
			剩余本金 = 本金 - 本额等息
		# print(本金,剩余本金)
		# print(剩余本金)c
		return 剩余本金

	lo, hi = 0.0, 100.0
	while abs(hi - lo) > err_rate:
		mid = (lo + hi) / 2.0
		# print(lo,mid,hi)
		err = get_err(本金, mid)
		if abs(err) > err_rate:
			if err > 0:
				hi = mid
			else:
				lo = mid
	return lo

	#calc_interset(45,107,7)
	#print(lo) #27.901...
	#print(get_err(本金,27.91)) #0.0496