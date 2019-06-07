select 
m.name,m.aproximated_ege,m.sex,m.rescue_date, p.name, p.last_name
from 
adopcion_person p 
inner join
Mascota_pet m 
on 
p.id=m.persons_id 
where 
lower(p.name)=lower('edgar') 