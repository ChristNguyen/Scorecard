# Scorecard
Scorecard and credit risk development for many method
Some feature need to focus: Otimal bining, automatic bining, unbalanced data, Bootsted tree method, logicstic model, reject reference.


**Giá trị KS	Khả năng phân loại của mô hình**
KS < 0.20	Mô hình không thích hợp để sử dụng
0.20 <= KS <= 0.40	Mô hình chấp nhận được
0.40 < KS <= 0.50	Mô hình tốt
KS > 0.50	Mô hình rất tốt
	
	
**Giá trị Gini	Khả năng phân loại của mô hình**
Gini < 0.20	Mô hình không thích hợp để sử dụng
0.20 <= Gini <= 0.40	Mô hình chấp nhận được
Gini > 0.40	Mô hình tốt
	
	
**Giá trị PSI	Tính ổn định của mô hình**
PSI <= 0.1	Mô hình ổn định, không có thay đổi đáng kể
0.1 < PSI <= 0.25	Mô hình thay đổi nhỏ, cần tìm hiểu nguyên nhân
PSI > 0.25	Mô hình có biến động lớn, cần xem xét hiệu chỉnh
	
  
**Thuật ngữ	Viết tắt**
Dữ liệu xây dựng mô hình	Train data
Dữ liệu kiểm định mô hình	Test data
"Số ngày quá hạn 
(Day Pass Due)"	DPD 
n MOB	n MOB
Tỷ trọng nợ quá hạn	%B2+
Tỷ trọng nợ xấu	%NPL
Khách hàng tốt	Good
Khách hàng xấu	Bad
Gini coefficient	Gini
"Kiểm định 
Kolmogorov-Smirnov"	KS
"Chỉ số ổn định của mô hình
(Population Stability Index)"	PSI

![image](https://user-images.githubusercontent.com/64264887/139172594-c2328bf7-6d4d-4abf-beb6-75bf26a7db03.png)

1. How exactly are the scorecard points calculated in the case of a binary target? and then converted into points based on the formula (scale mothod is PDO): 
	Score=A0+A1*ln(odd)
	A0=[600-20/ln(2)]/ln(50)
	A1=20/ln(2)
2. By default, missing values are transformed to 0. To apply the empirical transformation you have to set metric_special="empirical" and pass this information via the parameter binning_transform_params of the BinningProcess class. 

![image](https://user-images.githubusercontent.com/64264887/139182416-29f3697a-01e5-43d4-9462-dc3fcf6cd363.png)
