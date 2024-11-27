const express = require("express");
const morgan = require("morgan");
const cors = require("cors");
const { pool } = require("./db");
const app = express();
const port = process.env.PORT || 8000;
app.set("port", port);

app.use(cors());
app.use(morgan("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// web
app.post("/login", async (req, res) => {
        try {
                if (req.body.Member_ID && req.body.Password) {
                        const data = await pool.query(
                                `select * from Member where Member_ID = "${req.body.Member_ID}"`
                        );
                        if (data[0][0].Member_ID == req.body.Member_ID && data[0][0].password == req.body.Password) {
                                return res.json({
					login_token: true,
                                        Member_ID: req.body.Member_ID,
					Kiosk_ID: data[0][0].Kiosk_ID,
                                });
                        }
			else {
				res.status(403);
			}
                }
        } catch (error) {
                console.log(error);
        }
});

app.post("/signin", async (req, res) => {
        try {
                const data = await pool.query(
                        `insert into Member(Member_ID, Password, Name, Phone, Email, Kiosk_ID)
                        values("${req.body.Member_ID}", "${req.body.Password}", "${req.body.Name}", "${req.body.Phone}", "${req.body.Email}", "${req.body.Kiosk_ID}")`
                );
                return res.send({
                        signin_token: true, 
                        Member_ID: req.body.Member_ID,
                        Password: req.body.Password,
                        Name: req.body.Name,
                        Phone: req.body.Phone,
                        Email: req.body.Email,
                        Kiosk_ID: req.body.Kiosk_ID,
                });
        } catch (error) {
                console.log(error);
        }
});

app.post("/edit_member", async (req, res) => {
        try {
                const data = await pool.query(
                        `update Member
                        set Password = "${req.body.Password}",
                        Name = "${req.body.Name}",
                        Phone = "${req.body.Phone}",
                        Email = "${req.body.Email}",
                        Kiosk_ID = "${req.body.Kiosk_ID}"
                        where Member_ID = "${req.body.Member_ID}")`
                );
                return res.send({
                        edit_member_token: true,
                        Member_ID: req.body.Member_ID,
                        Password: req.body.Password,
                        Name: req.body.Name,
                        Phone: req.body.Phone,
                        Email: req.body.Email,
                        Kiosk_ID: req.body.Kiosk_ID,
                });
        } catch (error) {
                console.log(error);
        }
});

app.get("/id_check/:Member_ID", async (req, res) => {
        try {
                if (req.params.Member_ID) {
                        const data = await pool.query(
                                `select ifnull(max(Member_ID), 0) Member_ID from Member where Member_ID = "${req.params.Member_ID}"`
                        );
                        if (req.params.Member_ID == data[0][0].Member_ID) {
				res.status(403);
                        }
                        else {
                                return res.send("OK");
                        }
                }
        } catch (error) {
                console.log(error);
        }
});

app.get("/main/:Kiosk_ID", async (req, res) => {
        try {
                if (req.params.Kiosk_ID) {
                        const data = await pool.query(
                                `select * from Inventory where Kiosk_ID = "${req.params.Kiosk_ID}"`
                        );
                        return res.json(data[0]);
                }
        } catch (error) {
                console.log(error);
        }
});

app.post("/main/:Kiosk_ID/info/edit", async (req, res) => {
        try {
                const data = await pool.query(
                        `update Inventory
                        set Price = ${req.body.Price},
                        Amount = ${req.body.Amount},
                        Recommend = ${req.body.Recommend}
                        where Kiosk_ID = "${req.body.Kiosk_ID}"
			and Liq_ID = ${req.body.Liq_ID}`
                );
                return res.send({
                        edit_token: true,
                        Price: req.body.Price,
                        Amount: req.body.Amount,
                        Recommend: req.body.Recommend,
                        Kiosk_ID: req.body.Kiosk_ID,
                        Liq_ID: req.body.Liq_ID,
                });
        } catch (error) {
                console.log(error);
        }
});

app.post("/main/:Kiosk_ID/add/:Liq_ID", async (req, res) => {
        try {
                const data = await pool.query(
                        `select * from Liquor where Liq_ID = ${req.body.Liq_ID}`
                );
                const data2 = await pool.query(
                        `insert into Inventory(Liq_ID, Liq_Name, Price, Amount, Recommend, Count, Kiosk_ID)
                        values (${req.body.Liq_ID}, "${data[0][0].Name}", 0, 0, 0, 0, "${req.body.Kiosk_ID}")`
                );
                return res.send({
                        edit_token: true,
                        Liq_ID: req.body.Liq_ID,
                        Liq_Name: data[0][0].Name,
                        Price: 0,
                        Amount: 0,
                        Recommend: 0,
                        Count: 0,
                        Kiosk_ID: req.body.Kiosk_ID,
                });
        } catch (error) {
                console.log(error);
        }
});

app.delete("/main/:Kiosk_ID/delete/:Liq_ID", async (req, res) => {
        try {
                if (req.body.Liq_ID && req.body.Kiosk_ID) {
                        const data = await pool.query(
                                `delete from Inventory where Liq_ID = "${req.body.liq_id}" and Kiosk_ID = "${req.body.Kiosk_ID}"`
                        );

                        return res.json({
                                delete_token: true,
                                Liq_ID: req.body.Liq_ID,
                                Kiosk_ID: req.body.Kiosk_ID,
                        });
                }
        } catch (error) {
                console.log(error);
        }
});

app.get("/graph/:Kiosk_ID/whole", async (req, res) => {
        try {
                if (req.params.Kiosk_ID) {
                        const data = await pool.query(
                                `select Liq_Name, Count from Inventory
                                where Kiosk_ID = "${req.params.Kiosk_ID}"
                                ORDER BY Count DESC LIMIT 5`
                        );
                        return res.json(data[0]);
                }
        } catch (error) {
                console.log(error);
        }
});

app.get("/graph/:Kiosk_ID/whisky", async (req, res) => {
        try {
                if (req.params.Kiosk_ID) {
                        const data = await pool.query(
                                `select Liq_Name, Count, Category from Inventory natural join Liquor
                                where Kiosk_ID = "${req.params.Kiosk_ID}"
				and Category = "위스키"
                                ORDER BY Count DESC LIMIT 5`
                        );
                        return res.json(data[0]);
                }
        } catch (error) {
                console.log(error);
        }
});

app.get("/graph/:Kiosk_ID/liqueur", async (req, res) => {
        try {
                if (req.params.Kiosk_ID) {
                        const data = await pool.query(
                                `select Liq_Name, Count, Category from Inventory natural join Liquor
                                where Kiosk_ID = "${req.params.Kiosk_ID}"
				and Category = "리큐르"
                                ORDER BY Count DESC LIMIT 5`
                        );
                        return res.json(data[0]);
                }
        } catch (error) {
                console.log(error);
        }
});

app.get("/graph/:Kiosk_ID/vodka", async (req, res) => {
        try {
                if (req.params.Kiosk_ID) {
                        const data = await pool.query(
                                `select Liq_Name, Count, Category from Inventory natural join Liquor
                                where Kiosk_ID = "${req.params.Kiosk_ID}"
				and Category = "보드카"
                                ORDER BY Count DESC LIMIT 5`
                        );
                        return res.json(data[0]);
                }
        } catch (error) {
                console.log(error);
        }
});

app.get("/main/:Kiosk_ID/add_get/:Name", async (req, res) => {
        try {
                if (req.params.Name) {
                        const data = await pool.query(
                                `select * from Liquor where Name like "%${req.params.Name}%"`
                        );
                        return res.json(data[0]);
                }
        } catch (error) {
                console.log(error);
        }
});

app.post("/request", async (req, res) => {
        try {
                var today = new Date();

                var year = today.getFullYear();
                var month = ('0' + (today.getMonth() + 1)).slice(-2);
                var day = ('0' + today.getDate()).slice(-2);
                var hours = ('0' + today.getHours()).slice(-2);
                var minutes = ('0' + today.getMinutes()).slice(-2);
                var seconds = ('0' + today.getSeconds()).slice(-2);

                const dateString = year + '-' + month  + '-' + day + 'T' + hours + ':' + minutes  + ':' + seconds;

		await console.log(req.body.Text);
		await console.log(dateString);
                const data = await pool.query(
                        `insert into Request(Text, Date)
                        values("${req.body.Text}", "${dateString}")`
                );
                return res.send({
                        request_token: true, 
                        Text: req.body.Text,
                        Date: dateString,
                });
        } catch (error) {
                console.log(error);
        }
});

// kiosk
app.get("/kiosk/survey", async (req, res) => {
	try {
		const data = await pool.query(
			`select * from Survey`
		);
		return res.json(data[0]);
	} catch (error) {
		console.log(error);
	}
});

app.get("/kiosk/result", async (req, res) => {
        try {
                await console.log(req.body);
                // const data = await pool.query(
                //         `select `
                // )
                return res.send("servey result");
        } catch (error){
		console.log(error);
        }
});

app.post("/kiosk/count", async (req, res) => {
        try {
                await console.log(req.body);
                // const data = await pool.query(
                //         `select `
                // )
                return res.send("count up");
        } catch (error){
		console.log(error);
        }
});

app.get("/kiosk/face", async (req, res) => {
        try {
                await console.log(req.body);
                // const data = await pool.query(
                //         `select `
                // )
                return res.send("servey result");
        } catch (error){
		console.log(error);
        }
});

app.listen(app.get("port"), () => {
  console.log(`this server listening on ${app.get("port")}`);
});

