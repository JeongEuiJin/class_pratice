from car_kia import Car, Car_company



car_list=[]

def action():
    print('선택해주세요')
    car_store_property = 100000000
    car_customer_property = 50000000
    car_product_count = 231
    car_customer_count = 1

    while True:

        choice = input('원하시는게 무엇인가요\n1. 차종류입력\n2. 살게요\n3. 안살게요 안녕히계세요\n선택해주세요')
        if choice == '3':
            break
        elif choice =='1':
            car_name = input('차이름 :')
            car_price = input('차가격 :')
            car_color = input('차색상 :')
            color_brand = input('브랜드 :')
            new_car = Car_company(car_name,car_price,car_color,color_brand)
            car_list.append(new_car)


        elif choice=='2':
            if len(car_list) != 0:
                car_num = input("몇번 사실래요?")
                car_num = int(car_num)
                target_car = car_list[car_num]
                car_customer_property -= int(target_car.price)
                car_store_property += int(target_car.price)
                car_product_count-=1
                car_customer_count+=1

                print('구매후 고객의 재산{}\n판매후 차상점의 재산 {}\n판매후 차상점의 차 댓수 변화{}\n구매후 고객의 보유차량 댓수{}'.format(car_customer_property, car_store_property, car_product_count, car_customer_count))

            else:
                print('1번 부터 먼저 입력해주세요')






'''
class Sales:

    def car_ssles(self,name,price)
'''


action()

#trax.car