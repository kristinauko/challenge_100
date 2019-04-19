"""Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, a(i) and (i, 0). Find two lines, 
which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2."""


def find_max_area(container_list):
	"""Take the list of container heights and find max posible size of container"""

	max_container = 0

	for i in range(len(container_list)):

		container_size = 1

		for j in range(i+1, len(container_list)):

			if container_list[i] >= container_list[j]:
				container_size = container_list[j] * (j - i)
			else:
				container_size = container_list[i] * (j - i)

			if max_container < container_size:
				max_container = container_size

	return max_container


print(find_max_area([1,8,6,2,5,4,8,3,7]))