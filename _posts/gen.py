import os

lines = ['---\n','layout: post\n','title: ','date: 2017-12-20\n','category: LeetCode\n','tag: algorithm\n','---\n','\n','* content\n','{:toc}\n','\n','\n','```java\n']
titles = []
with open('titles', 'r') as tf:
	titles = tf.readlines()
titles = titles[1::2]

os.chdir("/Users/liujing/Documents/LeetCode/LeetCode/src")

for x in os.listdir("."):
	if os.path.isfile(x) and os.path.splitext(x)[1]=='.java':
		num = x.split('_')[1]
		name = x.split('_')[2].split('.')[0]

		if(int(num) > 109):
			continue

		codef = open(x,'r')
		txt = codef.readlines()

		with open('/Users/liujing/Documents/github/blog/_posts/2017-12-20-'+num+'-'+name+'.md', 'w') as f:

			lines[2] = 'title: '+num+'. '+titles[int(num)-1]
			f.writelines(lines)
			f.writelines(txt)
			f.write('```\n')

