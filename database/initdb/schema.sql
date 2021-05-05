GRANT ALL PRIVILEGES ON ds.* TO 'kavi'@'%'
use ds;
CREATE TABLE Rating
{
    id int not null auto_increment,
    rating int not null,
    primary key(id)
};