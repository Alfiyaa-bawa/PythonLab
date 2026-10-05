my_dict={'banana':3,'apple':1,'cherry':2,'date':4}
print("orginal list:",my_dict)
asorted_dict=dict(sorted(my_dict.items()))
print("Ascending order:",asorted_dict)
desorted_dict=dict(sorted(my_dict.items(),reverse=True))
print("Desending Order:",desorted_dict) 
